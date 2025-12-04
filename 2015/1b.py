with open("1.txt", "r") as file:
    s = file.readline().strip()
    f = 0
    for i,c in enumerate(s):
        f += -1 if c==")" else 1
        print(f)
        if f < 0:
            print(i+1)
            break