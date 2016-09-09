#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

lowerChar = 'abcdefghijklmnopqrstuvwxyz'
upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

fString = ''
for c in s:
    if 97 <= ord(c) <=122:
        lch = (lowerChar.index(c) + k ) % 26 
        fString += lowerChar[lch]
    elif 65 <= ord(c) <= 90:
        lch = (upperChar.index(c) + k ) % 26
        fString += upperChar[lch]
    else:
        fString += c
        
print fString