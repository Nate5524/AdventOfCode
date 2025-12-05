with open("./2015/5.txt", "r") as file:
    t=0
    for line in file:
        p=''
        d=False
        v=0
        k=True
        for c in line.strip():
            v+=int(c in"aeiou")
            d|=p==c
            k&=p+c not in["ab","cd","pq","xy"]
            p=c
        if k and d and v>2:t+=1
    print(t)