# -*- coding: utf-8 -*-

import boxsdk

def authenticate(identifier, secret, token): 
    '''identifier: client_id, provided in config.py
    secret: client_secret, provided in config.py
    token: developer token, accessed from box developer console
    '''
    oauth = boxsdk.OAuth2(
        client_id=identifier, 
        client_secret=secret, 
        access_token=token
    )
    client = boxsdk.Client(oauth)
    return client
