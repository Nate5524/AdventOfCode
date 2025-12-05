with open("5.txt", "r") as file:
    r=[]
    while (l:=file.readline().strip()) != "":
        a,b=map(int,l.split("-"))
        r.append((a,b))
    t=0
    for l in file:
        n=int(l.strip())
        for a,b in r:
            if a<=n<=b:
                t+=1
                break
    print(t)