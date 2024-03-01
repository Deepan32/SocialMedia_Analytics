import json
import pandas as pd
import numpy as np
import requests

def getCreds():
    """ Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""
    creds = dict()
    creds['access_token'] = 'EAAEedthbkBUBOZBfya3SGnt6De4wd6f3bSLfRpZBuxzqgITZBtNRZApvf3Vpx4xZAVcVVCFFdPzJeGpTZARIIbupFyH3vZAHZCjz0DMuR07aJcMGrOZAJ13sjL63OXMoxv6Kwjp0oo86mX9TNYZClWgzVlOrDfzfsECfX5CSrJ1lBQDNc4Cfd6fWFqT9ZCQWDZCojij45WSEoR5sVWcJRD36kI4H4ZBLDVICr8ZCApapdh9r4NBF7IB2yGqaFXheOPWti5gsAZD'
    creds['client_id'] = '314970761564181'
    creds['client_secret'] = 'a92327ba81ad881701c92a6ec2724ae1'
    creds['graph_domain']='https://graph.facebook.com'
    creds['graph_version']='v19.0'
    creds['endpoint_base']=creds['graph_domain']+creds['graph_version']+'/'
    creds['debug'] = 'no' # debug mode for api call
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

