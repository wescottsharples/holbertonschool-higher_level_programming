#!/usr/bin/python3
"""fetch https://intranet.hbtn.io/status"""

from sys import argv
import requests

r = requests.get(argv[1])
print(r.headers.get("X-Request-Id"))
