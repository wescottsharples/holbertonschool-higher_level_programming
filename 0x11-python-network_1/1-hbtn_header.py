#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL"""

from sys import argv
import urllib.request

rq = urllib.request.Request(argv[1])
with urllib.request.urlopen(rq) as rp:
    print(rp.getheader('X-Request-Id'))
