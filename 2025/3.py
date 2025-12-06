t=0
with open("./3.txt", "r") as file:
    for s in file:
        s = s.strip()
        l=[int(x) for x in s]
        m1 = max(l[:-1])
        m2 = max(l[l.index(m1)+1:])
        t += 10*m1+m2
print(t)