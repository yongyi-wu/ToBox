# -*- coding: utf-8 -*-

import pprint

import boxsdk


def list_folder_remote(folder, recurse=-1): 
    '''folder: a folder (boxsdk.object.folder.Folder) to inspect its content
    recurse: -1 nonrecursive, 0 recursive
    '''
    # TODO: make the display nicer
    if not isinstance(folder, boxsdk.object.folder.Folder): 
        raise ValueError('Invalid input')
    if recurse == -1: 
        # non-recursive case
        pprint.pprint(folder.get()['item_collection']['entries'])
    else: 
        # recursive case
        items = folder.get()['item_collection']['entries']
        pprint.PrettyPrinter(indent=recurse).pprint(items)
        subfolders = [item for item in items if isinstance(item, boxsdk.object.folder.Folder)]
        for subfolder in subfolders: 
            list_folder_remote(subfolder, recurse+1)
