import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
v = int(input())

time = 0
cList = []
nList = []
rTime = [0]*r

for i in range(v):
    c, n = [int(j) for j in input().split()]
    cList.append(c)
    nList.append(n)
    
if r >= v:
    for i in range(v):
        rTime[i] = (10**nList[i]) * (5**(cList[i]-nList[i]))
else:
    for i in range(r):
        rTime[i] = (10**nList[i]) * (5**(cList[i]-nList[i]))    
    
    rTime.sort()
    for i in range(r, v):
        rTime[0] += (10**nList[i]) * (5**(cList[i]-nList[i]))
        rTime.sort()
        
time = rTime[-1]
print(time)