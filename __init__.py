from airflow.plugins_manager import AirflowPlugin
from HubspotPlugin.hooks.hubspot_hook import HubspotHook
from HubspotPlugin.operators.hubspot_to_s3_operator import HubspotToS3Operator


class HubspotPlugin(AirflowPlugin):
    name = "hubspot_plugin"
    operators = [HubspotToS3Operator]
    hooks = [HubspotHook]
