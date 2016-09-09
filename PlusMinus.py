#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

negativeNumber = 0
positiveNumber = 0
zero = 0
for i in arr:
    if i < 0:
        negativeNumber+=1
    elif i > 0:
        positiveNumber+=1
    else:
        zero+=1
print format(positiveNumber/float(len(arr)),'.6f')
print format(negativeNumber/float(len(arr)),'.6f')
print format(zero/float(len(arr)),'.6f')