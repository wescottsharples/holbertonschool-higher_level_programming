#!/usr/bin/python3
for c in range(0, 90):
    if (c != 89):
        if ((c // 10) < (c % 10)):
            print("{:02d}".format(c), end=", ")
    else:
        print("{:02d}".format(c))
