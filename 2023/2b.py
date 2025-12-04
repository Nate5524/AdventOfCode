with open("2.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.split(":")[1]
        r,g,b=0,0,0
        for case in line.split(";"):
            case = case.split()
            for i in range(0,len(case),2):
                if case[i+1][0]== "r" and int(case[i]) > r:
                    r = int(case[i])
                if case[i+1][0]== "g" and int(case[i]) > g:
                    g = int(case[i])
                if case[i+1][0]== "b" and int(case[i]) > b:
                    b = int(case[i])
        sum += r*g*b
    print(sum)