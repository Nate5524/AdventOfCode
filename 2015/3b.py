with open("./2015/3.txt", "r") as file:
    s = file.readline().strip()
    x=y=a=b=0
    h={(0,0)}
    for i in range(0,len(s),2):
        match s[i]:
            case '>':
                x+=1
            case '<':
                x-=1
            case '^':
                y+=1
            case 'v':
                y-=1
        match s[i+1]:
            case '>':
                a+=1
            case '<':
                a-=1
            case '^':
                b+=1
            case 'v':
                b-=1
        h.update(((x,y),(a,b)))
    print(len(h))