from defines import getCreds, makeApiCall
import requests

def getUserPages( params):
    """ Get info on an access token 
        
        API Endpoint:
            https://graph.facebook.com/(graph-api-version}/me/accounts?access_token={access-token)

        Returns:
            object: data from the endpoint

    """
    end_point_params=dict()
    end_point_params["access_token"]=params["access_token"]
    url=params["endpoint_base"]+'me'
    return(makeApiCall(url,end_point_params,params['debug']))

params=getCreds()
params['debug']='yes'
response=getUserPages(params)


url=params["endpoint_base"]+"122116774574229875"

ACCESS_TOKEN="EAANBJ3EUqtQBOZBvMIfhmQY6ZCZBm84sLfuMG1SsHdDZCsB4keo8RXbR7i024WPfJ1fVdM6u4AQzOPaGjZBIDn1JZC5ZClMsuZCvoEHxBQEqLmWZCbsSFZAOnU3LpuZBsjGjyy0IQSaniCfKOluP782ptVZCapbuDOfFjDnmDyNcKfMn5f8BjlwK64fu4oR4IatxbMul"
url = f'https://graph.facebook.com/me?access_token={ACCESS_TOKEN}'
response = requests.get(url)

response.status_code
# Assuming the first page is the one you're interested in
id=response.json()['id']




# Things to solve:
# 1. The defines module is not getting refreshed. Any changes that are done there are not reflected.
