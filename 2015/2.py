with open("./2015/2.txt", "r") as file:
    t=0
    for line in file:
        l,w,h=map(int,line.strip().split("x"))
        s=[l*w,w*h,h*l]
        t+=min(s)+sum((2*x for x in s))
    print(t)