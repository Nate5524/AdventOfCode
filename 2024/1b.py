import sys
from collections import defaultdict

A = []
B = defaultdict(int)
with open("1.txt", "r") as file:
    for line in file:
        a,b = line.split()
        A.append(int(a))
        B[int(b)] += 1
    A.sort()
    total = 0
    
    for a in A:
        total += a*B[a]
    print(total)