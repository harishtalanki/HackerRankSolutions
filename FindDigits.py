#!/bin/python

import sys


t = int(raw_input().strip())

for a0 in xrange(t):
    n = int(raw_input().strip())
    strOfn=str(n)
    count = 0
    for i in strOfn:
        if int(i)==0:
            continue
        if (n%int(i) == 0):
            count +=1
    print count