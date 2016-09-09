#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    x = [i for i in a if i<=0]
    if k > len(x):
        print "YES"
    else:
        print "NO"
