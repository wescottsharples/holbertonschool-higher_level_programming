#!/usr/bin/python3
"""fetch https://intranet.hbtn.io/status"""

from sys import argv
import requests

if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.get(argv[1], data=payload)
    print(r.text)
