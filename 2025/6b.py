with open("6.txt", "r") as file:
    s = [l[:-1] for l in file]
    o = s.pop()
    t = 0
    p=[]
    for x in range(-1, -len(s[0])-1, -1):
        n = ""
        for y in range(len(s)):
            n += s[y][x]
        n = n.strip()
        if len(n) > 0: 
            p.append(n)
        else:
            t += eval(o[x+1].join(p))
            p.clear()
    t += eval(o[0].join(p))
    print(t)