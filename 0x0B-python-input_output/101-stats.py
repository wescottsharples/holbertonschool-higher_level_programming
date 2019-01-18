#!/usr/bin/python3
""" Script to parse stats from HTTP requests """
import sys

codes = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500": 0}
size = 0
count = 0


def print_codes():
    print("File size: {:d}".format(size))
    for i in sorted(codes.keys()):
        if codes[i] != 0:
            print("{:s}: {:d}".format(i, codes[i]))

try:
    for line in sys.stdin:
        info = list(map(str, line.strip().split(" ")))
        size += int(info[-1])
        if info[-2] in codes:
            codes[info[-2]] += 1
        count += 1
        if count % 10 == 0:
            print_codes()
except KeyboardInterrupt:
    print_codes()
