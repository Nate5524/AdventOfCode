with open("7.txt", "r") as file:
    numOk=0
    for line in file:
        x = line.split()
        ans = int(x[0][:-1])
        vals = [int(n) for n in x[1:]]
        poss = set()
        poss.add(vals[0])
        for v in vals[1:]:
            po = set()
            for p in poss:
                po.add(p+v)
                po.add(p-v)
                po.add(p*v)
                po.add(p//v)
            poss.update(po)
        if ans in poss: numOk += ans
    print(numOk)