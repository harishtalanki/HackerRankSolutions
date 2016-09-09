# Enter your code here. Read input from STDIN. Print output to STDOUT

def findMaxSum(li):
    sum = 0
    for element in li:
        if element > 0:
            sum += element
    if (sum == 0):
        return max(li)
    return sum

# Brute force
'''
def findMaxContiguousSum(li):
    sum1 = 0
    for i in range(0,len(li)+1):
        for j in range(0,i+1):
            if (sum(li[j:i]) > sum1):
                #print sumOfList(li[i:j])
                sum1 = sum(li[j:i])
    return sum1
'''

# Optimal
def findMaxContiguousSum(li):
    currentMaximum = li[0]
    finalMaximum = li[0]
    
    for i in range(1,len(li)):
        currentMaximum = max(li[i], currentMaximum + li[i])
        finalMaximum = max(finalMaximum, currentMaximum)
    return finalMaximum
    
n = int(raw_input())
for i in range(0,n):
    numberOfElements = int(raw_input())
    newList = raw_input().split()
    newList = [int(i) for i in newList]
    print str(findMaxContiguousSum(newList))+" "+str(findMaxSum(newList))