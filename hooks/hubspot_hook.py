from airflow.hooks.http_hook import HttpHook


class HubspotHook(HttpHook):

    def __init__(self, hubspot_conn_id):
        super().__init__(method='GET', http_conn_id=hubspot_conn_id)

    def run(self, endpoint, data=None, headers=None):
        conn = self.get_connection(self.http_conn_id)

        if conn.extra_dejson.get('hapikey'):
            self.hapikey = conn.extra_dejson.get('hapikey')
            data['hapikey'] = self.hapikey
        else:
            headers = {"Authorization": "Bearer {0}".format(conn.password)}
        return super().run(endpoint, data, headers)
