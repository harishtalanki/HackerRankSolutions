# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def isSquare(m):
    n = int(math.sqrt(m));
    return m == n*n
    
t = int(raw_input().strip())


for a0 in xrange(t):
    n = raw_input().strip().split()
    numOfSquares = 0
    temp = 0
    for i in xrange(int(n[0]), int(n[1])+1):
        if isSquare(i):
            numOfSquares += 1
            temp = math.sqrt(i) + 1
            break
            
    while temp != 0 and temp*temp <= int(n[1]):
        numOfSquares += 1
        temp += 1
    print numOfSquares