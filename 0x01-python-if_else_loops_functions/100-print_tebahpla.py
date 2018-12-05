#!/usr/bin/python3
for c in range(ord('Z'), ord('A') - 1, -1):
    print("{}".format(chr(c + ((c + 1) % 2) * 32)), end='')
