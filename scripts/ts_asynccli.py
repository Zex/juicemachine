#!/usr/bin/env python3

import requests

"""
resp = requests.get(
    'http://localhost:15113/juicemachine/flavor',
    headers={'Content-type':'application/json'})

print(resp.content)
"""

def generic_cb(resp, *args, **kwargs):
    print('[RESP-ARGS]', args)
    print('[RESP-KWARGS]', args, kwargs)
    #print("[RESP] ------------------>\n", resp.json())

resp = requests.get(
    'http://localhost:15113/juicemachine/flavor',
    headers={'Content-type':'application/json'},
    hooks={'response':generic_cb})

