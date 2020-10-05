# -*- coding: utf-8 -*-

import os

import boxsdk


def match_by_name(folder, name): 
    files = folder.get()['item_collection']['entries']
    for f in files: 
        if f['name'] == name: 
            return f
    return None


def get_item(client, working_dir, locator, kind): 
    '''locator: id or path to find the item
    kind: file_id, dir_id, path
    '''
    if kind == 'file_id': 
        try: 
            return client.file(file_id=locator).get()
        except: 
            raise ValueError('Invalid file id')
    elif kind == 'dir_id': 
        try: 
            return client.folder(folder_id=locator).get()
        except: 
            raise ValueError('Invalid folder id')
    elif kind == 'path': 
        locator = os.path.normpath(locator)
        tokens = locator.split(os.sep)
        if len(tokens) == 0: 
            raise ValueError('Invalid path')
        item = working_dir
        for name in tokens: 
            item = match_by_name(item, name)
            if item is None: 
                raise ValueError('Nonexist item: {}'.format(name))
        return item.get()
    else: 
        raise ValueError('Item id or path is required')


def make_if_nonexist_remote(folder, name): 
    '''folder: an existing remote folder (boxsdk.object.folder.Folder)
    name: the name (string) of subfolder to check
    '''
    subfolder = match_by_name(folder, name)
    if subfolder is None or not isinstance(subfolder, boxsdk.object.folder.Folder): 
        subfolder = folder.create_subfolder(name)
        print('New folder created: {}'.format(subfolder))
    return subfolder



def make_if_nonexist_local(folder, name): 
    '''folder: the path (string) to an existing local folder
    name: the name (string) of subfolder to check
    '''
    path = os.path.join(folder, name)
    print(path)
    if not os.path.exists(path): 
        os.mkdir(path)
        print('New directory created: {}'.format(path))
    return path
