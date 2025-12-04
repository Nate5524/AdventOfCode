from collections import defaultdict
with open("5.txt", "r") as file:
    #input
    flip = False
    rules = defaultdict(list)
    cases = []
    for line in file:
        line = line.strip()
        if line == "": flip = True
        elif flip: cases.append(line)
        else: 
            a,b = line.split("|")
            rules[b].append(a)
    total = 0
    for case in cases:
        c = case.split(",")
        err = False
        for i in range(1,len(c)):
            for j in range(i, -1, -1):
                if c[i] in rules[c[j]]:
                    err = True
                    break
            if err : break
        if not err: total += int(c[len(c)//2])
    print(total)