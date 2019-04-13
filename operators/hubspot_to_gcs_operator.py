from airflow.utils.decorators import apply_defaults

from airflow.models import BaseOperator, Variable, SkipMixin
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from HubspotPlugin.hooks.hubspot_hook import HubspotHook

from flatten_json import flatten
from os import path
import datetime
import logging
import json
import time
import boa


class HubspotToGCSOperator(BaseOperator, SkipMixin):
    """
    Hubspot To GCS Operator

    NOTE: A number of endpoints have nested arrays
    that are moved into their own table. In situations
    like this, the secondary table will have the prefix
    of the main Hubspot object.

    Example: The "Form Submissions" list of dictionaries
    in the contacts object will become it's own table
    with the label "contacts_form_submissions".

    :param hubspot_conn_id:          The Hubspot connection id.
    :type hubspot_conn_id:           string
    :param hubspot_object:           The desired Hubspot object. The currently
                                     supported values are:
                                        - campaigns
                                        - companies
                                        - contacts
                                        - contacts_by_company
                                        - deals
                                        - deal_pipelines
                                        - events
                                        - engagements
                                        - forms
                                        - keywords
                                        - lists
                                        - social
                                        - owners
                                        - timeline
                                        - workflows
    :type hubspot_object:            string
    :param hubspot_args:             Any additional arguments being sent to
                                     Hubspot to filter or format the results.
                                     Acceptable parameters will vary by object
                                     being requested. See Hubspot documentation
                                     for more details.
    :type hubspot_args:              dict
    :param gcs_conn_id:               The GCS connection id.
    :type gcs_conn_id:                string
    :param gcs_bucket:                The GCS bucket to be used to store
                                     the Hubspot data.
    :type gcs_bucket:                 string
    :param gcs_object:                   The GCS object to be used to store
                                     the Hubspot data.
    :type gcs_object:                    string
    """

    template_fields = ('gcs_object',
                       'hubspot_args',)

    @apply_defaults
    def __init__(self,
                 hubspot_conn_id,
                 hubspot_object,
                 gcs_conn_id,
                 gcs_bucket,
                 gcs_object,
                 hubspot_args={},
                 **kwargs):
        super().__init__(**kwargs)
        self.hubspot_conn_id = hubspot_conn_id
        self.hubspot_object = hubspot_object.lower()
        self.hubspot_args = hubspot_args
        self.gcs_conn_id = gcs_conn_id
        self.gcs_bucket = gcs_bucket
        self.gcs_object = gcs_object

        if self.hubspot_object not in ('campaigns',
                                       'companies',
                                       'contacts',
                                       'contacts_by_company',
                                       'deals',
                                       'deal_pipelines',
                                       'events',
                                       'engagements',
                                       'forms',
                                       'keywords',
                                       'lists',
                                       'owners',
                                       'social',
                                       'timeline',
                                       'workflows',):
            raise Exception('{0} is not a currently supported queryable object.'
                            .format(self.hubspot_object))

    def execute(self, context):
        h = HubspotHook(self.hubspot_conn_id)
        self.split = path.splitext(self.gcs_object)
        self.total_output_files = 0

        if self.hubspot_object == 'campaigns':
            campaigns = self.retrieve_data(h,
                                           context,
                                           "email/public/v1/campaigns")
            final_output = []
            for campaign in campaigns[0]['core']:
                logging.info("CAMPAIGN ID: " + str(campaign))
                output = self.retrieve_data(h,
                                            context,
                                            campaign_id=campaign['id'])
                output = output[0]['core']
                final_output.extend(output)
            self.outputManager(context,
                               final_output,
                               '{0}_core_final{1}'.format(self.split[0],
                                                          self.split[1]),
                               self.gcs_bucket)
        elif self.hubspot_object == 'contacts_by_company':
            companies = self.retrieve_data(h,
                                           context,
                                           endpoint=self.methodMapper('companies'))
            logging.info('Received companies list...')
            if not companies:
                logging.info('No companies currently available.')
                downstream_tasks = context['task'].get_flat_relatives(upstream=False)
                logging.info('Skipping downstream tasks...')
                logging.debug("Downstream task_ids %s", downstream_tasks)
                if downstream_tasks:
                    self.skip(context['dag_run'],
                              context['ti'].execution_date,
                              downstream_tasks)
                return True
            final_output = []

            for company in companies[0]['core']:
                output = self.retrieve_data(h,
                                            context,
                                            company_id=company['companyId'])
                final_output.extend(output)
            self.outputManager(context,
                               output,
                               '{0}_core_final{1}'.format(self.split[0],
                                                          self.split[1]),
                               self.gcs_bucket)
        else:
            output = self.retrieve_data(h, context)

            for e in output:
                for k, v in e.items():
                    if k == 'core':
                        key = '{0}_core_final{1}'.format(self.split[0],
                                                         self.split[1])
                    else:
                        key = '{0}_{1}_final{2}'.format(self.split[0],
                                                        k.lower().replace('.',
                                                                          '_'),
                                                        self.split[1])

                    self.outputManager(context,
                                       v,
                                       key,
                                       self.gcs_bucket)

            logging.info('Total Output File Count: ' + str(self.total_output_files))

    def outputManager(self, context, output, key, bucket):
        if len(output) == 0 or output is None:
            if self.total_output_files == 0:
                logging.info("No records pulled from Hubspot.")

                downstream_tasks = context['task'].get_flat_relatives(upstream=False)

                logging.info('Skipping downstream tasks...')
                logging.debug("Downstream task_ids %s", downstream_tasks)

                if downstream_tasks:
                    self.skip(context['dag_run'],
                              context['ti'].execution_date,
                              downstream_tasks)
        else:
            logging.info('Logging {0} to GCS...'.format(key))

            output = [flatten(e) for e in output]
            output = '\n'.join([json.dumps({boa.constrict(k): v
                               for k, v in i.items()}) for i in output])

            gcs = GoogleCloudStorageHook(self.gcs_conn_id)

            with open("__temp__", "w") as fid:
                fid.write(output)

            gcs_conn.upload(self.gcs_bucket, self.gcs_object, "__temp__")

            self.total_output_files += 1

    def retrieve_data(self,
                      h,
                      context,
                      endpoint=None,
                      company_id=None,
                      campaign_id=None):
        if endpoint is None:
            endpoint = self.methodMapper(self.hubspot_object,
                                         company_id=company_id,
                                         campaign_id=campaign_id)

        return self.paginate_data(h,
                                  endpoint,
                                  context,
                                  company_id=company_id,
                                  campaign_id=campaign_id)

    def paginate_data(self,
                      h,
                      endpoint,
                      context,
                      company_id=None,
                      campaign_id=None):
        """
        This method takes care of request building and pagination.
        It retrieves 100 at a time and continues to make
        subsequent requests until it retrieves less than 100 records.
        """
        output = []
        try:
            initial_offset = Variable.get('INCREMENTAL_KEY__{0}_{1}_vidOffset'.format(context['ti'].dag_id,
                                                                                      context['ti'].task_id))
            print('INITIAL OFFSET: ' + str(initial_offset))
        except:
            initial_offset = 0

        final_payload = {'vidOffset': initial_offset}

        if self.hubspot_object in ('events', 'timeline'):
            final_payload['limit'] = 1000
        elif self.hubspot_object == 'deals':
            final_payload['limit'] = 250
        elif self.hubspot_object == 'contacts':
            final_payload['count'] = 100

        for param in self.hubspot_args:
            # If time used as filter in request and is a string object
            # (e.g. when using {{ execution_date}}), convert the timestamp
            # to Hubspot formatting as needed by Hubspot API.
            if param in ('startTimestamp', 'endTimestamp'):
                param_time = datetime.datetime.strptime(self.hubspot_args[param],
                                                        "%Y-%m-%d %H:%M:%S")
                self.hubspot_args[param] = int(time.mktime(param_time.timetuple())
                                               * 1000)
            final_payload[param] = self.hubspot_args[param]
        logging.info('FINAL PAYLOAD: ' + str(final_payload))
        response = h.run(endpoint, final_payload).json()
        if not response:
            logging.info('Resource Unavailable.')
            return ''
        if self.hubspot_object == 'owners':
            output.extend([e for e in response])
            # output = [self.filterMapper(record) for record in output]
            output = self.subTableMapper(output)
            return output
        elif self.hubspot_object == 'engagements':
            output.extend([e for e in response['results']])
        elif self.hubspot_object == 'contacts_by_company':
            if endpoint == 'companies/v2/companies/paged':
                if response['companies']:
                    output.extend([e for e in response['companies']])
                else:
                    logging.info('No companies currently available.')
                    return ''
            else:
                output.extend([{"vid": e, "company_id": company_id}
                               for e in response['vids']])
        elif self.hubspot_object == 'campaigns':
            if 'email/public/v1/campaigns/' in endpoint:
                output.append(response)
        elif self.hubspot_object in ('deal_pipelines', 'social'):
                output.extend([e for e in response])
        else:
            output.extend([e for e in response[self.hubspot_object]])

        if isinstance(response, dict):
            if 'hasMore' in list(response.keys()):
                more = 'hasMore'
            elif 'has-more' in list(response.keys()):
                more = 'has-more'
            else:
                more = 'has-more'
                response['has-more'] = False
            n = 0

            if 'vid-offset' in list(response.keys()):
                offset_variable = 'vid-offset'
            elif 'offset' in list(response.keys()):
                offset_variable = 'offset'

            while response[more] is True:
                if offset_variable == 'vid-offset':
                    final_payload['vidOffset'] = response['vid-offset']
                    logging.info('Retrieving: ' + str(response['vid-offset']))
                elif offset_variable == 'offset':
                    final_payload['offset'] = response['offset']
                    logging.info('Retrieving: ' + str(response['offset']))
                try:
                    response = h.run(endpoint, final_payload).json()
                except:
                    pass

                if endpoint == 'companies/v2/companies/paged':
                    if response['companies']:
                        output.extend([e for e in response['companies']])
                else:
                    output.extend([e for e in response[self.hubspot_object]])

                n += 1
                time.sleep(0.2)
                if n % 50 == 0:
                    # output = [self.filterMapper(record) for record in output]
                    output = self.subTableMapper(output)
                    if self.hubspot_object == 'contacts_by_company':
                        companies = self.retrieve_data(h, self.methodMapper('companies'))
                        if not companies:
                            logging.info('No companies currently available.')
                            downstream_tasks = context['task'].get_flat_relatives(upstream=False)
                            logging.info('Skipping downstream tasks...')
                            logging.debug("Downstream task_ids %s", downstream_tasks)
                            if downstream_tasks:
                                self.skip(context['dag_run'], context['ti'].execution_date, downstream_tasks)
                            return True
                        final_output = []
                        for company in companies:
                            final_output.extend(output)
                        key = '{0}_core_{1}{2}'.format(self.split[0],
                                                       str(n),
                                                       self.split[1])
                        self.outputManager(context,
                                           output,
                                           key,
                                           self.gcs_bucket)

                    else:
                        for e in output:
                            for k, v in e.items():
                                if k == 'core':
                                    key = '{0}_core_{1}{2}'.format(self.split[0],
                                                                   str(n),
                                                                   self.split[1])
                                else:
                                    key = '{0}_{1}_{2}{3}'.format(self.split[0],
                                                                  boa.constrict(k),
                                                                  str(n),
                                                                  self.split[1])
                                logging.info('Sending to Output Manager...')
                                self.outputManager(context,
                                                   v,
                                                   key,
                                                   self.gcs_bucket)
                                if self.hubspot_object == 'contacts':
                                    if response[offset_variable] == 0:
                                        logging.info('No new records received.')
                                        logging.info('Offset variable is still: ' + str(initial_offset))
                                    else:
                                        new_offset = ('INCREMENTAL_KEY__{0}_{1}_vidOffset'
                                                      .format(context['ti'].dag_id,
                                                              context['ti'].task_id))
                                        logging.info('New Variable offset is now: ' +\
                                                     str(response[offset_variable]))

                                        Variable.set(new_offset, response[offset_variable])

                    output = []

            if self.hubspot_object == 'contacts':
                if response[offset_variable] == 0:
                    logging.info('No new records received.')
                    logging.info('Offset variable is still: ' + str(initial_offset))
                else:
                    new_offset = ('INCREMENTAL_KEY__{0}_{1}_vidOffset'
                                  .format(context['ti'].dag_id,
                                          context['ti'].task_id))
                    logging.info('New Variable offset is now: ' + str(response[offset_variable]))

                    Variable.set(new_offset, response[offset_variable])


        # output = [self.filterMapper(record) for record in output]
        output = self.subTableMapper(output)

        return output

    def methodMapper(self, hubspot_object, company_id=None, campaign_id=None):
        """
        This method maps the desired object to the relevant endpoint
        according to v3 of the Hubspot API.
        """
        mapping = {"campaigns": "email/public/v1/campaigns/{0}"
                                .format(campaign_id),
                   "companies": "companies/v2/companies/paged",
                   "contacts": "contacts/v1/lists/all/contacts/all",
                   "contacts_by_company": "companies/v2/companies/{0}/vids"
                                          .format(company_id),
                   "deals": "deals/v1/deal/paged",
                   "deal_pipelines": "/deals/v1/pipelines",
                   "events": "email/public/v1/events",
                   "engagements": "engagements/v1/engagements/paged",
                   "forms": "forms/v2/forms",
                   "keywords": "keywords/v1/keywords",
                   "lists": "contacts/v1/lists",
                   "social": "broadcast/v1/channels/setting/publish/current",
                   "owners": "owners/v2/owners",
                   "timeline": "email/public/v1/subscriptions/timeline",
                   "workflows": "automation/v3/workflows"
                   }

        return mapping[hubspot_object]

    def subTableMapper(self, output):
        """
        This mapper expects a list of either dictionaries
        or string values as specified in the 'split' value
        of the mapping and then outputs them to a new object.
        """
        mapping = [{'name': 'contacts',
                    'split': 'form-submissions',
                    'retained': []
                    },
                   {'name': 'contacts',
                    'split': 'identity-profiles',
                    'retained': [{"addedAt": "addedAt"}]
                    },
                   {'name': 'contacts',
                    'split': 'merge-audits',
                    'retained': [{'vid': 'vid'}]
                    },
                   {'name': 'contacts',
                    'split': 'merged-vids',
                    'retained': [{"vid": "vid"}]
                    },
                   {'name': 'contacts',
                    'split': 'list-memberships',
                    'retained': []
                    },
                   {'name': 'deals',
                    'split': 'associations.associatedVids',
                    'retained': [{"dealId": "deal_id"}]
                    },
                   {'name': 'deals',
                    'split': 'associations.associatedCompanyIds',
                    'retained': [{"dealId": "deal_id"}]
                    },
                   {'name': 'deals',
                    'split': 'associations.associatedDealIds',
                    'retained': [{"dealId": "deal_id"}]
                    },
                   {'name': 'deal_pipelines',
                    'split': 'stages',
                    'retained': [{"pipelineId": "pipeline_id"}]
                    },
                   {'name': 'forms',
                    'split': 'formFieldGroups',
                    'retained': [{'guid': 'form_id'}]
                    },
                   {'name': 'lists',
                    'split': 'filters',
                    'retained': []
                    },
                   {'name': 'owners',
                    'split': 'remoteList',
                    'retained': []
                    },
                   {'name': 'timeline',
                    'split': 'changes',
                    'retained': [{'timestamp': 'timestamp'},
                                 {'recipient': 'recipient'}]
                    },
                   {'name': 'workflows',
                    'split': 'personaTagIds',
                    'retained': [{'id': 'workflow_id'}]
                    },
                   {'name': 'workflows',
                    'split': 'contactListIds.steps',
                    'retained': [{'id': 'workflow_id'}]
                    }]

        def process_record(record, mapping):
            final_returnable_dict = {}

            def getByDotNotation(obj, ref):
                val = obj
                try:
                    for key in ref.split('.'):
                        val = val[key]
                except:
                    val = False
                return val

            for entry in mapping:
                returnable_list = []
                subtable_data = getByDotNotation(record, entry['split'])
                if ((entry['name'] == self.hubspot_object) and subtable_data):
                    final_key_split = entry['split'].lower().replace('.', '_')
                    for item in subtable_data:
                        returnable_dict = {}
                        if isinstance(item, dict):
                            returnable_dict = item
                        elif isinstance(item, str) or isinstance(item, int):
                            returnable_dict[final_key_split] = item
                        for item in entry['retained']:
                            for k, v in item.items():
                                try:
                                    returnable_dict[v] = record[k]
                                except KeyError:
                                    logging.info(record)
                                    logging.info(returnable_dict[v])
                        returnable_list.append(returnable_dict)

                if returnable_list:
                    final_returnable_dict[entry['split']] = returnable_list

                final_returnable_dict['core'] = record
            return final_returnable_dict

        def process_data(output):
            output = [process_record(record, mapping) for record in output]
            output_list = []
            output_dict = {}
            output_dict['core'] = [e.pop('core') for e in output]
            output_list.append(output_dict)
            for entry in mapping:
                output_dict = {}
                if (entry['name'] == self.hubspot_object):
                    output_dict[entry['split']] = [e.pop(entry['split']) for e in output
                                                   if (entry['split'] in list(e.keys()))]
                    output_dict[entry['split']] = [item for sublist in output_dict[entry['split']]
                                                   for item in sublist]
                    if not output_dict[entry['split']]:
                        del output_dict[entry['split']]
                    output_list.append(output_dict)
            output_list = [e for e in output_list if e]

            return output_list

        return process_data(output)

    def filterMapper(self, record):
        """
        This process strips out unnecessary objects (i.e. ones
        that are duplicated in other core objects).
        """
        mapping = [{'name': 'commits',
                    'filtered': 'author',
                    'retained': ['id']
                    }]

        def process(record, mapping):
            """
            This method processes the data according to the above mapping.
            There are a number of checks throughout as the specified filtered
            object and desired retained fields will not always exist in each
            record.
            """

            for entry in mapping:
                # Check to see if the filtered value exists in the record
                if (entry['name'] == self.hubspot_object)\
                 and (entry['filtered'] in list(record.keys())):
                    # Check to see if any retained fields are desired.
                    # If not, delete the object.
                    if entry['retained']:
                        for retained_item in entry['retained']:
                            # Check to see the filterable object exists in the
                            # specific record. This is not always the case.
                            # Check to see the retained field exists in the
                            # filterable object.
                            if record[entry['filtered']] is not None\
                             and retained_item in list(record[entry['filtered']].keys()):
                                # Bring retained field to top level of
                                # object with snakecasing.
                                record["{0}_{1}".format(entry['filtered'],
                                                        retained_item)] = \
                                    record[entry['filtered']][retained_item]
                    if record[entry['filtered']] is not None:
                        del record[entry['filtered']]

            return record

        return process(record, mapping)
