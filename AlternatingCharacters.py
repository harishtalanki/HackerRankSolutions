# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
stringList = []

for i in range(0,n):
    stringList.append(raw_input())
    
def findNumberOfDeletions(word):
    wordCount = 0
    for i in range(0,len(word)-1):
        if word[i] == word[i+1]:
            wordCount = wordCount + 1
    return wordCount      
    
for s in stringList:
    print findNumberOfDeletions(s)