# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
d={}
avg = 0.00
for line in fileinput.input():
    lol = line.split()
    if len(lol) > 1:
        d[lol[0]] = lol[1:]
    else:
        if line > 1:
            nameToSearch = lol[0]
            
for key in d.keys():
    if key == nameToSearch:
        vals = d[key]
        for i in vals:
            avg = avg + float(i)
        pass
print format(avg/3,'.2f')