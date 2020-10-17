# -*- coding: utf-8 -*-

import argparse


def tokenize(commands, cmd): 
    '''cmd: a string from standard input
    '''
    tokens = cmd.split()
    # recover whitespace in quotation mark and remove quotation mark
    i = 0
    while i < len(tokens): 
        if tokens[i].startswith('\'') or tokens[i].startswith('\"'): 
            seen = True
            c = tokens[i][0]
            j = i
            while j < len(tokens): 
                if tokens[j].endswith(c): 
                    tokens = tokens[:i] + [' '.join(tokens[i:j+1])[1:-1]] + tokens[j+1:]
                    i += 1
                    seen = False
                    break
                else: 
                    j += 1
            if seen: 
                raise ValueError('Odd number of quotation mark')
        else: 
            i += 1
    if len(tokens) == 0 or tokens[0] not in commands: 
        raise ValueError('Invalid command name')
    return tokens


def parse_tokens(tokens): 
    '''cmd: a list of tokens similar to sys.argv
    '''
    parser = argparse.ArgumentParser()
    command = tokens[0]
    if command in ['help', 'quit']: 
        pass
    elif command == 'cd': 
        parser.add_argument('dst', type=str, help='path of the new working directory')
    elif command == 'ls': 
        parser.add_argument('--dst', type=str, help='folder to inspect content')
        parser.add_argument('-r', action='store_true', default=False, help='whether to recursively ls subfolders')
    elif command in ['upload', 'download']: 
        parser.add_argument('--file', action='store_true', default=True, help='indicate to upload files (default)')
        parser.add_argument('--folder', action='store_true', help='indicate to upload folder')
        if command == 'upload': 
            parser.add_argument('src', type=str, nargs='+', help='source path on local machine to upload from')
            parser.add_argument('dst', type=str, help='remote folder id or path to upload to')
        elif command == 'download': 
            parser.add_argument('src', type=str, nargs='+', help='remote id or path to download from')
            parser.add_argument('dst', type=str, help='destination path on local machine to download to')
    params = parser.parse_args(tokens[1:])
    return (command, params)


def parse(commands, cmd): 
    tokens = tokenize(commands, cmd)
    params = parse_tokens(tokens)
    return params


if __name__ == '__main__': 
    commands = set(['quit', 'help', 'cd', 'ls', 'upload', 'download'])
    while True: 
        cmd = input('test: ')
        print(parse(commands, cmd))
