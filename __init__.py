from airflow.plugins_manager import AirflowPlugin
from HubspotPlugin.hooks.hubspot_hook import HubspotHook
from HubspotPlugin.operators.hubspot_to_s3_operator import HubspotToS3Operator
from HubspotPlugin.operators.hubspot_to_gcs_operator import HubspotToGCSOperator


class HubspotPlugin(AirflowPlugin):
    name = "hubspot_plugin"
    operators = [HubspotToS3Operator, HubspotToGCSOperator]
    hooks = [HubspotHook]
