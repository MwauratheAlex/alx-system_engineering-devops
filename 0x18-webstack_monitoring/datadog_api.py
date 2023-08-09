"""
Get the total number of active hosts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)

    try:
        response = api_instance.list_hosts()
        print(response["host_list"])
    except Exception as e:
        message = '''DD_SITE="datadoghq.com" DD_API_KEY="<YOUR_API_KEY>"'''
        message += ''' DD_APP_KEY="<YOUR_APP_KEY" python3 datadog_api.py'''

        print("Usage: < {} >\n".format(message))
        print("{}".format(e))
