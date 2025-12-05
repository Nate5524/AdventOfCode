with open("./2015/3.txt", "r") as file:
    s = file.readline().strip()
    x=y=0
    h={(0,0)}
    for c in s:
        match c:
            case '>':
                x+=1
            case '<':
                x-=1
            case '^':
                y+=1
            case 'v':
                y-=1
        h.add((x,y))
    print(len(h))