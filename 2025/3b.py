t=0
with open("./3.txt", "r") as file:
    for s in file:
        s = s.strip()
        l=[0]+[int(x) for x in s]
        d = [0]
        v=0
        for i in range(11,-1,-1):
            v=v+l[v:].index(d[-1])+1
            x = max(l[v:-i] if i>0 else l[v:])
            d.append(x)
        n=int("".join(map(str,d)))
        t += n
print(t)