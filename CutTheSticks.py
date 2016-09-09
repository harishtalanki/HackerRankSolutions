#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print len(arr)
noSticks = True
while noSticks:
    small = min(arr)
    arr = [i-small for i in arr if i-small != 0]
    if len(arr) <= 0:
        noSticks = False
    else:
        print len(arr)