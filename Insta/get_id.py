from defines import getCreds, makeApicall

def getUserPages( params):
    """ Get info on an access token 
        
        API Endpoint:
            https://graph.facebook.com/(graph-api-version}/me/accounts?access_token={access-token)

        Returns:
            object: data from the endpoint

    """
    end_point_params=dict()
    end_point_params["access_token"]=params["access_token"]
    url=params["endpoint_base"]+'me/accounts'
    return(makeApicall(url,end_point_params,params['debug']))


params=getCreds()




