#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    choc = n/c
    wrappers = choc
    while wrappers >= m:
        choc += 1
        wrappers +=1
        wrappers -=m
    print choc