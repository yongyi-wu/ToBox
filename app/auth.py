# -*- coding: utf-8 -*-

import boxsdk


def authenticate(box_id, box_secret, dev_token): 
    oauth = boxsdk.OAuth2(
        client_id=box_id, 
        client_secret=box_secret, 
        access_token=dev_token
    )
    client = boxsdk.Client(oauth)
    print('The current user ID is {0}'.format(client.user().get().id))
    return client
