import sys

A = []
B = []
with open("1.txt", "r") as file:
    for line in file:
        a,b = line.split()
        A.append(int(a))
        B.append(int(b))
    A.sort()
    B.sort()
    total = 0
    for i in range(len(A)):
        total += abs(A[i]-B[i])
    print(total)