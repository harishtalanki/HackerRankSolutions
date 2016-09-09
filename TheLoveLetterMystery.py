# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
stringList = []

for i in range(0,n):
    stringList.append(raw_input())
    
def numberOfreductions(s):
    reductions = 0
    for i in range(0,len(s)/2):
        reductions += abs(ord(s[i])-ord(s[-1-i]))
    return reductions
    
for eachString in stringList:
    print numberOfreductions(eachString)