# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
newString = [i.lower() if i.isupper() else i.upper() for i in n]
print "".join(newString)