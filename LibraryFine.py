#!/bin/python

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

y= y1 - y2
if y == 0:
    m = m1 - m2
    if m == 0:
        if d1 <= d2:
            print 0
        else:
            print str(15*(d1-d2))
    elif (m > 0):
        print str(500*(m))
    else:
        print 0
elif (y > 0):
    print 10000
else:
    print 0