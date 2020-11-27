# -*- coding: utf-8 -*-

import argparse

from main import ToBox


client_id = 'FILL THIS PART'
client_secret = 'FILL THIS PART'


if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('client_token', type=str, help='Please refer to help/get_tokens.pdf for instructions')
    args = parser.parse_args()
    ToBox(client_id, client_secret, args.client_token)
