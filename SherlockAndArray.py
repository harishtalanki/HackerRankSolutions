# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

n = int(raw_input())
finalList = []
newList = []

def findSherlockArray(newArr, tsum, sumLeft):
    for i in range(1,len(newArr)):
        sumRight = 0
        sumLeft += newArr[i-1]
        sumRight = tsum - sumLeft - newArr[i]
        #print newArr[i]
        #print "totalSum is:"+str(tsum)
        #print sumLeft
        #print sumRight
        if sumLeft == sumRight:
            return "YES"
    return "NO"

for i in range(0,n):
    numberOfChars = int(raw_input())
    listToWork = list(map(int, sys.stdin.readline().split()))
    sumLeft = 0
    totalSum = 0
    totalSum=sum(listToWork)
    if len(listToWork) == 1:
        print "YES"
        continue
    else:
        print findSherlockArray(listToWork, totalSum, sumLeft)