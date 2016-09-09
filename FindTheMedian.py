# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
arrList = [int(i) for i in raw_input().split()]
print sorted(arrList)[len(arrList)/2]