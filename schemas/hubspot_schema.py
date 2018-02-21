
"""
Campaigns

First need to make a request to
https://developers.hubspot.com/docs/methods/email/get_campaigns

Then pass campaign ids into
https://developers.hubspot.com/docs/methods/email/get_campaign_data
and concatenate the results.
"""

campaigns = [{"name": "app_id",
              "type": "bigint"},
             {"name": "app_name",
              "type": "varchar(256)"},
             {"name": "content_id",
              "type": "bigint"},
             {"name": "counters_delivered",
              "type": "bigint"},
             {"name": "counters_deferred",
              "type": "bigint"},
             {"name": "counters_dropped",
              "type": "bigint"},
             {"name": "counters_unsubscribed",
              "type": "bigint"},
             {"name": "counters_bounce",
              "type": "bigint"},
             {"name": "counters_open",
              "type": "bigint"},
             {"name": "counters_processed",
              "type": "bigint"},
             {"name": "counters_sent",
              "type": "bigint"},
             {"name": "counters_click",
              "type": "bigint"},
             {"name": "counters_spamreport",
              "type": "bigint"},
             {"name": "counters_mta_dropped",
              "type": "bigint"},
             {"name": "counters_forward",
              "type": "bigint"},
             {"name": "counters_statuschange",
              "type": "bigint"},
             {"name": "counters_selected",
              "type": "bigint"},
             {"name": "id",
              "type": "int"},
             {"name": "group_id",
              "type": "int"},
             {"name": "name",
              "type": "varchar(512)"},
             {"name": "num_included",
              "type": "int"},
             {"name": "num_queued",
              "type": "int"},
             {"name": "sub_type",
              "type": "varchar(256)"},
             {"name": "subject",
              "type": "varchar(512)"},
             {"name": "type",
              "type": "varchar(256)"},
             {"name": "processing_state",
              "type": "varchar(256)"}]


"""
Companies
https://developers.hubspot.com/docs/methods/companies/get-all-companies

"""
companies = [{"name": "portal_id",
              "type": "int"},
             {"name": "properties_website_source_id",
              "type": "varchar(256)"},
             {"name": "properties_website_timestamp",
              "type": "timestamp"},
             {"name": "properties_website_value",
              "type": "varchar(256)"},
             {"name": "properties_website_source",
              "type": "varchar(256)"},
             {"name": "properties_name_source_id",
             "type": "varchar(256)"},
             {"name": "properties_name_timestamp",
              "type": "timestamp"},
             {"name": "properties_name_value",
              "type": "varchar(256)"},
             {"name": "properties_name_source",
              "type": "varchar(256)"},
             {"name": "is_deleted",
              "type": "boolean"},
             {"name": "company_id",
              "type": "int"}
             ]

"""
Contact Lists
    - Core
    - Filters

https://developers.hubspot.com/docs/methods/lists/get_lists
"""

lists = [{"name": "parent_id",
          "type": "int"},
         {"name": "dynamic",
          "type": "boolean"},
         {"name": "meta_data_processing",
          "type": "varchar(256)"},
         {"name": "meta_data_size",
          "type": "int"},
         {"name": "meta_data_error",
          "type": "varchar(256)"},
         {"name": "meta_data_last_processing_state_change_at",
          "type": "timestamp"},
         {"name": "meta_data_last_size_change_at",
          "type": "timestamp"},
         {"name": "portal_id",
          "type": "int"},
         {"name": "created_at",
          "type": "timestamp"},
         {"name": "list_id",
          "type": "int"},
         {"name": "updated_at",
          "type": "timestamp"},
         {"name": "list_type",
          "type": "varchar(256)"},
         {"name": "internal_list_id",
          "type": "int"},
         {"name": "deleteable",
          "type": "boolean"}]


lists_filters = [{"name": "list_id",
                  "type": "varchar(256)"},
                 {"name": "within_time_mode",
                  "type": "varchar(256)"},
                 {"name": "check_past_versions",
                  "type": "boolean"},
                 {"name": "filter_family",
                  "type": "varchar(256)"},
                 {"name": "type",
                  "type": "varchar(256)"},
                 {"name": "property",
                  "type": "varchar(256)"},
                 {"name": "value",
                  "type": "varchar(256)"},
                 {"name": "operator",
                  "type": "varchar(256)"}]


"""
Contacts
    - Core
    - Form Submissions
    - Identity Profiles
    - List Memberships
    - Merge Audits
    - Merged Vids

https://developers.hubspot.com/docs/methods/contacts/get_contacts
"""
contacts = [{"name": "vid",
             "type": "bigint"},
            {"name": "iscontact",
             "type": "boolean"},
            {"name": "profileurl",
             "type": "varchar(512)"},
            {"name": "rating",
             "type": "varchar(512)"},
            {"name": "portalid",
             "type": "bigint"},
            {"name": "added_at",
             "type": "timestamp"},
            {"name": "mergedvids",
             "type": "text"},
            {"name": "profiletoken",
             "type": "varchar(256)"},
            {"name": "verical",
             "type": "varchar(256)"},
            {"name": "annualrevenue",
             "type": "varchar(512)"},
            {"name": "academic_subvertical",
             "type": "varchar(512)"},
            {"name": "properties_firstname_value",
             "type": "varchar(256)"},
            {"name": "properties_lastname_value",
             "type": "varchar(256)"},
            {"name": "properties_company_value",
             "type": "varchar(256)"},
            {"name": "properties_lastmodifieddate_value",
             "type": "bigint"},
            {"name": "properties_createdate_value",
             "type": "bigint"},
            {"name": "properties_state_value",
             "type": "varchar(256)"},
            {"name": "properties_zip_value",
             "type": "varchar(256)"},
            {"name": "properties_address_value",
             "type": "varchar(512)"},
            {"name": "properties_city_value",
             "type": "varchar(512)"},
            {"name": "properties_twitterbio_value",
             "type": "varchar(256)"},
            {"name": "properties_twitterhandle_value",
             "type": "varchar(256)"},
            {"name": "properties_twitterprofilephoto_value",
             "type": "varchar(512)"},
            {"name": "canonicalvid",
             "type": "int"}]

contacts_formsubmissions = [{"name": "conversionid",
                             "type": "varchar(256)"},
                            {"name": "timestamp",
                             "type": "timestamp"},
                            {"name": "formid",
                             "type": "varchar(256)"},
                            {"name": "portalid",
                             "type": "int"},
                            {"name": "vid",
                             "type": "int"},
                            {"name": "pageid",
                             "type": "varchar(256)"},
                            {"name": "pageurl",
                             "type": "varchar(256)"},
                            {"name": "contenttype",
                             "type": "varchar(256)"},
                            {"name": "canonicalurl",
                             "type": "varchar(512)"},
                            {"name": "title",
                             "type": "varchar(512)"},
                            {"name": "pagetitle",
                             "type": "varchar(512)"},
                            {"name": "metadata",
                             "type": "varchar(max)"}]

contacts_identityprofiles = [{"name": "vid",
                              "type": "int"},
                             {"name": "added_at",
                              "type": "timestamp"},
                             {"name": "identities_0_timestamp",
                              "type": "bigint"},
                             {"name": "identities_0_isprimary",
                              "type": "boolean"},
                             {"name": "identities_0_issecondary",
                              "type": "boolean"},
                             {"name": "identities_0_type",
                              "type": "varchar(256)"},
                             {"name": "identities_0_value",
                              "type": "varchar(256)"},
                             {"name": "identities_1_timestamp",
                              "type": "timestamp"},
                             {"name": "identities_1_isprimary",
                              "type": "boolean"},
                             {"name": "identities_1_issecondary",
                              "type": "boolean"},
                             {"name": "identities_1_type",
                              "type": "varchar(256)"},
                             {"name": "identities_1_value",
                              "type": "varchar(256)"},
                             {"name": "identities_2_timestamp",
                              "type": "timestamp"},
                             {"name": "identities_2_isprimary",
                              "type": "boolean"},
                             {"name": "identities_2_issecondary",
                              "type": "boolean"},
                             {"name": "identities_2_type",
                              "type": "varchar(256)"},
                             {"name": "identities_2_value",
                              "type": "varchar(256)"},
                             {"name": "identities_3_timestamp",
                              "type": "timestamp"},
                             {"name": "identities_3_isprimary",
                              "type": "boolean"},
                             {"name": "identities_3_issecondary",
                              "type": "boolean"},
                             {"name": "identities_3_type",
                              "type": "varchar(256)"},
                             {"name": "identities_3_value",
                              "type": "varchar(256)"},
                             {"name": "savedattimestamp",
                              "type": "timestamp"},
                             {"name": "deletedchangedtimestamp",
                              "type": "timestamp"}]

contacts_listmemberships = [{"name": "static_list_id",
                              "type": "int"},
                             {"name": "internal_list_id",
                              "type": "int"},
                             {"name": "timestamp",
                              "type": "timestamp"},
                             {"name": "vid",
                              "type": "int"},
                             {"name": "is_member",
                             "type": "boolean"}]

contacts_mergeaudits = [{"name": "canonicalvid",
                         "type": "bigint"},
                        {"name": "vidtomerge",
                         "type": "bigint"},
                        {"name": "timestamp",
                         "type": "timestamp"},
                        {"name": "userid",
                         "type": "bigint"},
                        {"name": "vid",
                         "type": "bigint"},
                        {"name": "firstname",
                         "type": "varchar(256)"},
                        {"name": "lastname",
                         "type": "varchar(256)"},
                        {"name": "numpropertiesmoved",
                         "type": "int"},
                        {"name": "entityid",
                         "type": "text"},
                        {"name": "merged_from_email_value",
                         "type": "varchar(256)"},
                        {"name": "merged_from_email_source_type",
                         "type": "varchar(256)"},
                        {"name": "merged_from_email_source_id",
                         "type": "int"},
                        {"name": "merged_from_email_source_label",
                         "type": "varchar(256)"},
                        {"name": "merged_from_email_timestamp",
                         "type": "timestamp"},
                        {"name": "merged_to_email_value",
                         "type": "varchar(256)"},
                        {"name": "merged_to_email_source_type",
                         "type": "varchar(256)"},
                        {"name": "merged_to_email_source_id",
                         "type": "int"},
                        {"name": "merged_to_email_source_label",
                         "type": "varchar(256)"},
                        {"name": "merged_to_email_timestamp",
                         "type": "timestamp"}]

contacts_mergedvids = [{"name": "vid", "type": "int"},
                       {"name": "merged_vid", "type": "int"}]


"""
Contacts by Company

First need to make a request to
https://developers.hubspot.com/docs/methods/companies/get-all-companies

Then pass company ids into
https://developers.hubspot.com/docs/methods/companies/get_company_contacts_by_id
"""

contacts_by_company = [{"name": "contact_id", "type": "int"},
                       {"name": "company_id", "type": "int"}]

"""
Deals
https://developers.hubspot.com/docs/methods/deals/get-all-deals
    - Core
    - Deals Associations - Associated Vids
    - Deals Associations - Associated Company Ids
    - Deals Associations - Associated Deal Ids
"""

deals = [{"name": "portal_id",
          "type": "bigint"},
         {"name": "deal_id",
          "type": "bigint"},
         {"name": "description",
          "type": "varchar(max)"},
         {"name": "is_deleted",
          "type": "boolean"},
         {"name": "close_date",
          "type": "timestamp"},
         {"name": "create_date",
          "type": "timestamp"},
         {"name": "closed_won_reason",
          "type": "varchar(max)"},
         {"name": "closed_lost_reason",
          "type": "bigint"},
         {"name": "properties_amount_value",
          "type": "double precision"},
         {"name": "properties_amount_timestamp",
          "type": "timestamp"},
         {"name": "properties_amount_source_id",
          "type": "varchar(256)"},
         {"name": "properties_amount_source",
          "type": "varchar(256)"},
         {"name": "properties_dealname_value",
          "type": "varchar(256)"},
         {"name": "properties_dealname_timestamp",
          "type": "timestamp"},
         {"name": "properties_dealname_source",
          "type": "varchar(256)"},
         {"name": "properties_dealname_source_id",
          "type": "varchar(256)"}]

deals_associations_associatedvids = [{"name": "deal_id",
                                      "type": "varchar(256)"},
                                     {"name": "associated_vids",
                                      "type": "varchar(256)"}]

deals_associations_associatedcompanyvids = [{"name": "deal_id",
                                             "type": "varchar(256)"},
                                            {"name": "associated_company_vids",
                                             "type": "varchar(256)"}]

deals_associations_associateddealids = [{"name": "deal_id",
                                         "type": "varchar(256)"},
                                        {"name": "associated_deal_ids",
                                         "type": "varchar(256)"}]

"""
Deal Pipelines
https://developers.hubspot.com/docs/methods/deal-pipelines/get-all-deal-pipelines
"""
deal_pipelines = [{"name": "active",
                   "type": "boolean"},
                  {"name": "display_order",
                   "type": "int"},
                  {"name": "label",
                   "type": "varchar(256)"},
                  {"name": "pipeline_id",
                   "type": "varchar(256)"}]


deal_pipelines_stages = [{"name": "pipeline_id",
                          "type": "varchar(256)"},
                         {"name": "active",
                          "type": "boolean"},
                         {"name": "closed_won",
                          "type": "boolean"},
                         {"name": "display_order",
                          "type": "int"},
                         {"name": "label",
                          "type": "varchar(256)"},
                         {"name": "probability",
                          "type": "decimal(3,2)"},
                         {"name": "stage_id",
                          "type": "varchar(256)"}]

"""
Email Events
https://developers.hubspot.com/docs/methods/email/get_events
"""

events = [{"name": "app_id",
           "type": "int"},
          {"name": "app_name",
           "type": "varchar(256)"},
          {"name": "browser_family",
           "type": "varchar(256)"},
          {"name": "browser_name",
           "type": "varchar(256)"},
          {"name": "browser_producer",
           "type": "varchar(256)"},
          {"name": "browser_producer_url",
           "type": "varchar(256)"},
          {"name": "browser_type",
           "type": "varchar(256)"},
          {"name": "browser_url",
           "type": "varchar(256)"},
          {"name": "caused_by_event_id",
           "type": "varchar(256)"},
          {"name": "caused_by_event_created",
           "type": "varchar(256)"},
          {"name": "created",
           "type": "timestamp"},
          {"name": "device_type",
           "type": "varchar(256)"},
          {"name": "duration",
           "type": "int"},
          {"name": "email_campaign_id",
           "type": "int"},
          {"name": "hmid",
           "type": "varchar(256)"},
          {"name": "id",
           "type": "varchar(256)"},
          {"name": "ip_address",
           "type": "varchar(256)"},
          {"name": "location_city",
           "type": "varchar(256)"},
          {"name": "location_country",
           "type": "varchar(256)"},
          {"name": "location_state",
           "type": "varchar(256)"},
          {"name": "portal_id",
           "type": "int"},
          {"name": "recipient",
           "type": "varchar(256)"},
          {"name": "response",
           "type": "varchar(512)"},
          {"name": "sent_by_created",
           "type": "timestamp"},
          {"name": "sent_by_id",
           "type": "varchar(256)"},
          {"name": "smtp_id",
           "type": "varchar(256)"},
          {"name": "type",
           "type": "varchar(256)"},
          {"name": "user_agent",
           "type": "varchar(256)"}]


"""
Engagements
    - Core
    - Associations
    - Attachments

https://developers.hubspot.com/docs/methods/engagements/get-all-engagements
"""
engagements = [{"name": "engagement_id",
                "type": "bigint"},
               {"name": "engagement_portal_id",
                "type": "bigint"},
               {"name": "engagement_active",
                "type": "boolean"},
               {"name": "engagement_created_at",
                "type": "timestamp"},
               {"name": "engagement_created_by",
                "type": "bigint"},
               {"name": "engagement_modified_by",
                "type": "bigint"},
               {"name": "engagement_last_updated",
                "type": "timestamp"},
               {"name": "engagement_owner_id",
                "type": "bigint"},
               {"name": "engagement_type",
                "type": "varchar(256)"},
               {"name": "metadata_body",
                "type": "text"},
               {"name": "engagement_timestamp",
                "type": "bigint"},
               {"name": "associations_contact_ids_0",
                "type": "bigint"},
               {"name": "associations_contact_ids_1",
                "type": "bigint"},
               {"name": "associations_contact_ids_3",
                "type": "bigint"}]


# Associated object can be contact, company, or deal

engagements_associations = [{"name": "engagement_id",
                             "type": "int"},
                            {"name": "associated_id",
                             "type": "int"},
                            {"name": "associated_object",
                             "type": "varchar(256)"}]

engagements_attachments = [{"name": "engagement_id",
                            "type": "int"},
                           {"name": "attachment_id",
                            "type": "int"}]

"""
Forms
    - Core
    - Form Field Groups

https://developers.hubspot.com/docs/methods/forms/v2/get_forms
"""
forms = [{"name": "portal_id",
          "type": "int"},
         {"name": "guid",
          "type": "varchar(256)"},
         {"name": "name",
          "type": "varchar(256)"},
         {"name": "method",
          "type": "varchar(256)"},
         {"name": "css_class",
          "type": "varchar(256)"},
         {"name": "redirect",
          "type": "varchar(256)"},
         {"name": "submit_text",
          "type": "varchar(256)"},
         {"name": "notify_recipients",
          "type": "varchar(256)"},
         {"name": "created_at",
          "type": "timestamp"},
         {"name": "updated_at",
          "type": "timestamp"},
         {"name": "ignore_current_values",
         "type": "boolean"},
         {"name": "deletable",
          "type": "boolean"},
         {"name": "inline_message",
          "type": "varchar(256)"},
         {"name": "captcha_enabled",
          "type": "boolean"},
         {"name": "cloneable",
          "type": "boolean"},
         {"name": "editable",
          "type": "boolean"},
         {"name": "form_type",
          "type": "varchar(256)"},
         {"name": "deleted_at",
          "type": "timestamp"}
         ]


forms_fieldgroups = [{"name": "form_guid",
                      "type": "varchar(256)"},
                      {"name": "default",
                       "type": "boolean"},
                      {"name": "is_smart_group",
                       "type": "boolean"},
                      {"name": "rich_text_content",
                       "type": "varchar(256)"},
                      {"name": "name",
                       "type": "varchar(256)"},
                      {"name": "label",
                      "type": "varchar(256)"},
                      {"name": "type",
                       "type": "varchar(256)"},
                      {"name": "field_type",
                      "type": "varchar(256)"},
                      {"name": "description",
                       "type": "varchar(256)"},
                      {"name": "group_name",
                       "type": "varchar(256)"},
                      {"name": "display_order",
                       "type": "int"},
                      {"name": "required",
                      "type": "boolean"},
                      {"name": "selected_options",
                      "type": "varchar(256)"},
                      {"name": "options",
                       "type": "varchar(256)"},
                      {"name": "validation_name",
                      "type": "varchar(256)"},
                      {"name": "validation_message",
                       "type": "varchar(256)"},
                      {"name": "validation_data",
                       "type": "varchar(256)"},
                      {"name": "validation_use_default_block_list",
                      "type": "boolean"},
                      {"name": "validation_use_default_blocked_email_addresses",
                       "type": "varchar(256)"},
                      {"name": "hidden",
                      "type": "boolean"},
                      {"name": "default_value",
                       "type": "varchar(256)"},
                      {"name": "is_smart_field",
                      "type": "boolean"},
                      {"name": "placeholder",
                      "type": "varchar(256)"},
                      {"name": "dependent_field_filters",
                      "type": "varchar(256)"}]
"""
Keywords
https://developers.hubspot.com/docs/methods/keywords/get_keywords
"""

keywords = [{"name": "keyword",
             "type": "varchar(256)"},
            {"name": "keyword_guid",
             "type": "varchar(256)"},
            {"name": "country",
             "type": "int"},
            {"name": "visits",
             "type": "int"},
            {"name": "contacts",
             "type": "int"},
            {"name": "leads",
             "type": "int"},
            {"name": "created_at",
             "type": "timestamp"}]


"""
Owners
    - Core
    - Remote List

https://developers.hubspot.com/docs/methods/owners/get_owners
"""
owners = [{"name": "portal_id",
           "type": "int"},
          {"name": "owner_id",
           "type": "int"},
          {"name": "type",
           "type": "varchar(256)"},
          {"name": "first_name",
           "type": "varchar(256)"},
          {"name": "last_name",
           "type": "varchar(256)"},
          {"name": "email",
           "type": "varchar(256)"},
          {"name": "created_at",
           "type": "timestamp"},
          {"name": "updated_at",
           "type": "timestamp"}]

owners_remote_list = [{"name": "portal_id",
                      "type": "int"},
                      {"name": "owner_id",
                       "type": "int"},
                      {"name": "id",
                       "type": "int"},
                      {"name": "remote_id",
                       "type": "varchar(256)"},
                      {"name": "remote_type",
                       "type": "varchar(256)"},
                      {"name": "active",
                       "type": "boolean"}]


"""
Social
https://developers.hubspot.com/docs/methods/social_media/get_channels
"""
social = [{"name": "channel_slug",
           "type": "varchar(256)"},
          {"name": "account_slug",
           "type": "varchar(256)"},
          {"name": "channel_guid",
           "type": "varchar(256)"},
          {"name": "username",
           "type": "varchar(256)"},
          {"name": "name",
           "type": "varchar(256)"},
          {"name": "portal_id",
           "type": "bigint"},
          {"name": "channel_id",
           "type": "varchar(256)"},
          {"name": "twitter_id",
           "type": "bigint"},
          {"name": "account_guid",
           "type": "varchar(256)"},
          {"name": "created_at",
           "type": "timestamp"},
          {"name": "updated_at",
           "type": "timestamp"},
          {"name": "type",
           "type": "varchar(256)"},
          {"name": "account_type",
           "type": "varchar(256)"},
          {"name": "reach",
           "type": "boolean"},
          {"name": "reach_type",
           "type": "varchar(256)"},
          {"name": "auto_publish",
           "type": "boolean"},
          {"name": "active",
           "type": "boolean"},
          {"name": "twitter_screen_name",
           "type": "varchar(256)"},
          {"name": "avatar_url",
           "type": "varchar(256)"},
          {"name": "profile_url",
           "type": "varchar(256)"},
          {"name": "display_name",
           "type": "varchar(256)"},
          {"name": "channel_key",
           "type": "varchar(256)"},
          {"name": "follow_me",
           "type": "boolean"},
          {"name": "shared",
           "type": "boolean"},
          {"name": "hidden",
           "type": "boolean"},
          {"name": "monitoring",
           "type": "boolean"},
          {"name": "data_map_imageurl",
           "type": "varchar(256)"},
          {"name": "data_map_userid",
           "type": "varchar(256)"},
          {"name": "data_map_companyid",
           "type": "varchar(256)"},
          {"name": "data_map_username",
           "type": "varchar(256)"},
          {"name": "data_map_realname",
           "type": "varchar(256)"},
          {"name": "data_map_picture",
           "type": "varchar(256)"},
          {"name": "data_map_pictureurl",
           "type": "varchar(256)"},
          {"name": "data_map_pagename",
           "type": "varchar(256)"},
          {"name": "data_map_profileurl",
           "type": "varchar(256)"},
          {"name": "data_map_websiteurl",
           "type": "varchar(256)"},
          {"name": "data_map_email",
           "type": "varchar(256)"},
          {"name": "data_map_pageid",
           "type": "varchar(256)"},
          {"name": "data_map_name",
           "type": "varchar(256)"},
          {"name": "data_map_fullname",
           "type": "varchar(256)"},
          {"name": "data_map_firstname",
           "type": "varchar(256)"},
          {"name": "data_map_lastname",
           "type": "varchar(256)"},
          {"name": "data_map_pagecategory",
           "type": "varchar(256)"},
          {"name": "settings_followme",
           "type": "boolean"},
          {"name": "settings_monitoring",
           "type": "boolean"},
          {"name": "settings_autopublish",
           "type": "boolean"},
          {"name": "settings_publish",
           "type": "boolean"},
          {"name": "settings_reach",
           "type": "boolean"},
          {"name": "settings_hidden",
           "type": "boolean"},
          {"name": "channel_scopes",
           "type": "varchar(256)"}]

"""
Subscriptions Timeline
https://developers.hubspot.com/docs/methods/email/get_subscriptions_timeline
"""
timeline = [{"name": "timestamp",
             "type": "timestamp"},
            {"name": "recipient",
             "type": "varchar(256)"},
            {"name": "portal_id",
             "type": "bigint"}]

timeline_changes = [{"name": "timestamp",
                     "type": "timestamp"},
                    {"name": "portal_id",
                     "type": "bigint"},
                    {"name": "recipient",
                     "type": "varchar(256)"},
                    {"name": "source",
                     "type": "varchar(256)"},
                    {"name": "change",
                     "type": "varchar(256)"},
                    {"name": "change_type",
                     "type": "varchar(256)"},
                    {"name": "caused_by_event_id",
                     "type": "varchar(256)"},
                    {"name": "caused_by_event_created",
                     "type": "timestamp"}]

"""
Workflows
    - Core
    - Persona Tag ids
    - Contact List Ids - Steps

https://developers.hubspot.com/docs/methods/workflows/v3/get_workflows
"""

workflows = [{"name": "name",
              "type": "varchar(256)"},
             {"name": "id",
              "type": "int"},
             {"name": "enabled",
              "type": "boolean"},
             {"name": "inserted_at",
              "type": "timestamp"},
             {"name": "updated_at",
              "type": "timestamp"},
             {"name": "contact_listids_enrolled",
              "type": "int"},
             {"name": "contact_listids_active",
              "type": "int"}]

workflows_personatagids = [{"name": "workflow_id",
                             "type": "int"},
                            {"name": "personaTagIds",
                             "type": "int"}]

workflows_contactlistids_steps = [{"name": "workflow_id",
                                    "type": "int"},
                                   {"name": "contactListIds_steps",
                                    "type": "int"}]
