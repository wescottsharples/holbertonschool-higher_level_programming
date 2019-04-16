#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL"""

from sys import argv
from urllib import parse, request


if __name__ == '__main__':
    url = argv[1]
    values = {'emails': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    rq = request.Request(url, data)
    with urllib.request.urlopen(rq) as rp:
        print(rp.read().decode('utf-8'))
