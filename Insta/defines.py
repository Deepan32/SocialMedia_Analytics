import json
import pandas as pd
import numpy as np
import requests
import pandas as pd

def getCreds():
    """ Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""
    creds = dict()
    creds['access_token'] = 'EAANBJ3EUqtQBOZBvMIfhmQY6ZCZBm84sLfuMG1SsHdDZCsB4keo8RXbR7i024WPfJ1fVdM6u4AQzOPaGjZBIDn1JZC5ZClMsuZCvoEHxBQEqLmWZCbsSFZAOnU3LpuZBsjGjyy0IQSaniCfKOluP782ptVZCapbuDOfFjDnmDyNcKfMn5f8BjlwK64fu4oR4IatxbMul'
    creds['client_id'] = '916062586841812'
    creds['client_secret'] = 'ce7003dc0d99a045622305109ea34e6e'
    creds['graph_domain']='https://graph.facebook.com'
    creds['graph_version']='v19.0'
    creds['endpoint_base']=creds['graph_domain']+'/'+creds['graph_version']+'/'
    creds['debug'] = 'no' # debug mode for api call
    creds['page_id'] ='122116774574229875'
    return(creds)

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print("\nURL: ") # title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty']) # display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli


def makeApiCall(url, endpointPrams, debug = 'no'):
    data = requests.get( url, endpointPrams)
    response = dict()
    response['url']=url
    response['endpoint_params'] = endpointPrams
    response['endpoint_params_pretty'] = json.dumps(endpointPrams, indent = 4)
    response['json_data']=json.loads( data.content)
    response['json_data_pretty']=json.dumps(response['json_data'], indent = 4)

    if( debug =='yes'):
        displayApiCallData( response)
    
    return(response)

