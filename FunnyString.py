# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
wordList = []
for i in range(0,n):
    wordList.append(raw_input())
    
def reverseString(stringToReverse):
    return stringToReverse[::-1]

def findIfFunny(s):
    rString = reverseString(s)
    funnyString=False
    for i in range(0,len(s)-1):
        if abs(ord(s[i+1])-ord(s[i])) == abs(ord(rString[i+1])-ord(rString[i])):
            funnyString=True
        else:
            funnyString=False
            break
    if funnyString:
        return "Funny"
    else:
        return "Not Funny"
    

for word in wordList:
    print findIfFunny(word)