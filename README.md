# Plugin - Hubspot to S3

This plugin moves data from the [Hubspot](https://developers.hubspot.com/docs/overview) API to S3 based on the specified object

## Hooks
### HubspotHook
This hook handles the authentication and request to Hubspot. This extends the HttpHook.

### S3Hook
[Core Airflow S3Hook](https://pythonhosted.org/airflow/_modules/S3_hook.html) with the standard boto dependency.

## Operators
### HubspotToS3Operator
This operator composes the logic for this plugin. It fetches the Hubpsot specified object and saves the result in a S3 Bucket, under a specified key, in
njson format. The parameters it can accept include the following.

#### NOTE: A number of endpoints have nested arrays that are moved into their own table. In situations like this, the secondary table will have the prefix of the main Hubspot object.

  Example: The "Form Submissions" list of dictionaries in the contacts object will become it's own table with the label "contacts_form_submissions".

- `hubspot_conn_id`          The Hubspot connection id.
- `hubspot_object`           The desired Hubspot object. The currently
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
- `hubspot_args`             Any additional arguments being sent to
                             Hubspot to filter or format the results.
                             Acceptable parameters will vary by object
                             being requested. See Hubspot documentation
                             for more details.
- `s3_conn_id`               The s3 connection id.
- `s3_bucket`                The S3 bucket to be used to store the Hubspot data.
- `s3_key`                   The S3 key to be used to store the Hubspot data.

## Install


First we need to get the dependencies installed with:
```
pip3 install -r requirements.txt
```

Next step is to add the `$AIRFLOW_HOME/plugins` to the **PYTHONPATH**.
```
export PYTHONPATH="$PYTHONPATH:$AIRFLOW_HOME/plugins"
```
> this also works: `PYTHONPATH=$AIRFLOW_HOME/plugins airflow webserver`

Put the files from this repository on the Airflow Plugins directory

```
cp -rf ~/devel/hubspot_plugin/ $AIRFLOW_HOME/plugins
```

## Connections Settings _(`Airflow > Admin > Connections`)_

### Hubspot

Create a **HTTP** connection, filling the following fields:

 - **Host**: api.hubapi.com/
 - **Schema**: https
 - **Extra** with something like this:
    ```
    {"hapikey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}
    ```

### S3

Create a **S3** connection, filling the **Extra** field with something like this:
```
{"aws_access_key_id": "xxxxxxxxxxx", "aws_secret_access_key": "xxxxxxxxxxxxxxxxxx/xxxx"}
```
