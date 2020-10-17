# -*- coding: utf-8 -*-

import os

import boxsdk

from .utils import match_by_name, make_if_nonexist_local, make_if_nonexist_remote


def upload_files(srcs, dst): 
    '''srcs: a list of paths (strings) to local files
    dst: a target folder (boxsdk.object.folder.Folder)
    '''
    for src in srcs: 
        print('Uploading {}'.format(src), end='...')
        try: 
            name = os.path.basename(src)
            remote = match_by_name(dst, name)
            if remote is not None: 
                ans = input('{} already exists in {}. Update? y/[n]'.format(name, dst))
                if ans.lower() != 'y': 
                    print('Skip')
                    continue
                else: 
                    remote.update_contents(src)
            else: 
                dst.upload(src)
            print('Done')
        except: 
            print('Fails!')


def upload_folders(srcs, dst): 
    '''srcs: a list paths (strings) to local directories
    dst: a target folder (boxsdk.object.folder.Folder)
    '''

    def upload_folder_helper(src, dst): 
        '''src: a path (string) to a local directory
        dst: a target folder (boxsdk.object.folder.Folder)
        '''
        for root, dirs, files in os.walk(src): 
            folder = make_if_nonexist_remote(dst, os.path.basename(root))
            files = [os.path.join(root, f) for f in files]
            upload_files(files, folder)
            for name in dirs: 
                upload_folder_helper(os.path.join(root, name), folder)
            break

    for src in srcs: 
        upload_folder_helper(src, dst)


def download_files(srcs, dst): 
    '''srcs: a list of remote files (boxsdk.object.file.File)
    dst: a local directory (string)
    '''
    for src in srcs: 
        print('Downloading {}'.format(src), end='...')
        try: 
            name = os.path.join(dst, src['name'])
            if os.path.exists(name): 
                ans = input('{} already exists in {}. Overwrite? y/[n]'.format(src['name'], dst))
                if ans.lower() != 'y': 
                    print('Skip')
                    continue
            with open(name, 'wb') as f: 
                content = src.content()
                f.write(content)
            print('Done')
        except: 
            print('Fails!')


def download_folders(srcs, dst): 
    '''srcs: a list remote folders to be downloaded (boxsdk.object.folder.Folder)
    dst: a target local directory (string)
    '''

    def download_folder_helper(src, dst): 
        '''src: a remote folder to be downloaded (boxsdk.object.folder.Folder)
        dst: a target local directory (string)
        '''
        dst = make_if_nonexist_local(dst, src['name'])
        items = src.get()['item_collection']['entries']
        files = []
        subfolders = []
        for item in items: 
            if isinstance(item, boxsdk.object.folder.Folder): 
                subfolders.append(item)
            else: 
                files.append(item)
        download_files(files, dst)
        for subfolder in subfolders: 
            print(dst)
            print(subfolder['name'])
            download_folder_helper(subfolder, dst)

    for src in srcs: 
        download_folder_helper(src, dst)
