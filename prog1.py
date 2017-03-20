#!/usr/bin/env python2.7

import sys

print "Program that displays the even numbers entered by the user"
print "Enter the numbers you want to test followed by (Ctrl+d)"
results = []
for number in sys.stdin:
    number = number.strip()
    if int(number) % 2 == 0:
        results.append(number)

print "The even numbers are: "
print ' '.join(results)
