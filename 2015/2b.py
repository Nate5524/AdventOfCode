with open("./2015/2.txt", "r") as file:
    t=0
    for line in file:
        a,b,c=sorted(int(x) for x in line.strip().split("x"))
        t+=a+a+b+b+a*b*c
    print(t)