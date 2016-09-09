# Enter your code here. Read input from STDIN. Print output to STDOUT

first, second, nth = raw_input().split()

#temp = int(second) * int(second) + int(first) 
temp1 = 0

for i in range(3, int(nth)+1):
    temp1 = int(second) * int(second) + int(first)
    first = second
    second = temp1
print temp1