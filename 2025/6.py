with open("6.txt", "r") as file:
    s = [l.strip().split() for l in file]
    o = s.pop()
    t=0
    for i in range(len(s[0])):
        t+=eval(o[i].join([x[i] for x in s]))
    print(t)