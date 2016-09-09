# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sentence={}
for i in n:
    if (not i.isspace() and i.upper() in alphabet):
        if i.upper() in sentence:
            sentence[i.upper()] = sentence[i.upper()] + 1
        else:
            sentence[i.upper()] = 1

if len(sentence) == len(alphabet):
    print "pangram"
else:
    print "not pangram"