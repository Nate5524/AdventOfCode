with open("5.txt", "r") as file:
    r=[]
    while (l:=file.readline().strip()) != "":
        a,b=map(int,l.split("-"))
        r.append([a,b])
    r.sort()
    s=[r[0]]
    for i in range(1,len(r)):
        p=s[-1]
        c=r[i]
        if c[0] <= p[1]: p[1]=max(p[1],c[1])
        else: s.append(c)
    t=0
    for l,r in s: t+=r-l+1
    print(t)