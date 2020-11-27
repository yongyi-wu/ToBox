# -*- coding: utf-8 -*-

import os

import app


def scheduler(client, working_dir, command, params): 
    '''command: one of supported command key words
    params: optional and required arguments
    '''
    def get_item_helper(locator, kind): 
        '''locator: id or path to find the folder
        kind: folder or file
        '''
        if locator.isdigit(): 
            if kind == 'folder': 
                kind = 'dir_id'
            elif kind == 'file': 
                kind = 'file_id'
        else: 
            kind = 'path'
        return app.get_item(client, working_dir, locator, kind)

    if command == 'cd': 
        working_dir = get_item_helper(params.dst, 'folder')
        print('Current working directory: {}'.format(working_dir['name']))
    elif command == 'ls': 
        if params.dst is None: 
            folder = working_dir
        else: 
            folder = get_item_helper(params.dst, 'folder')
        if params.r: 
            recurse = 0
        else: 
            recurse = -1
        app.list_folder_remote(folder, recurse)
    elif command == 'upload': 
        srcs = [os.path.expanduser(src) for src in params.src]
        dst = get_item_helper(params.dst, 'folder')
        if not params.folder: 
            app.upload_files(srcs, dst)
        else: 
            app.upload_folders(srcs, dst)
    elif command == 'download': 
        srcs = []
        dst = os.path.expanduser(params.dst)
        if not params.folder: 
            for src in params.src: 
                srcs.append(get_item_helper(src, 'file'))
            app.download_files(srcs, dst)
        else: 
            for src in params.src: 
                srcs.append(get_item_helper(src, 'folder'))
            app.download_folders(srcs, dst)
    return working_dir


def ToBox(client_id, client_secret, client_token): 
    print('''\
##########################################################
#####  Welcome to the ToBox toolbox for HoltLab@CMU  #####
##########################################################
    ''')
    commands = set(['quit', 'help', 'cd', 'ls', 'upload', 'download'])
    print('Authenticating', end='...')
    client = app.authenticate(client_id, client_secret, client_token)
    try: 
        print('Done! {}'.format(client.user().get()))
    except: 
        print('Fail! Incorrect token(s)')
        return
    working_dir = client.folder(folder_id='0')
    while True: 
        cmd = input('\n>>> ')
        try: 
            (command, params) = app.parse(commands, cmd)
            if command == 'quit': 
                print('Bye!')
                break
            elif command == 'help': 
                print('Currently supported commands: {}.\nFor specific instruction, try: <command> --help'.format(commands))
            else: 
                working_dir = scheduler(client, working_dir, command, params)  
        except Exception as e: 
            print(e)
        except SystemExit: 
            pass
