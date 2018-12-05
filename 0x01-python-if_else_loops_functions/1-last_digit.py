#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
message = "Last digit of {} is {}"
greater = " and is greater than 5"
zero = " and is 0"
lesser = " and is less than 6 and not 0"
last_digit = abs(number) % 10

if (number < 0):
    last_digit = last_digit * -1

if (last_digit > 5):
    print(message.format(number, last_digit) + greater)
elif (last_digit == 0):
    print(message.format(number, last_digit) + zero)
else:
    print(message.format(number, last_digit) + lesser)
