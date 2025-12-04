with open("1.txt", "r") as file:
    total = 0
    dial = 50
    for line in file:
        c,n = line[0],int(line[1:])
        total += n // 100
        n = n % 100
        if c=="L":
            new = dial - n
            if new <= 0 and dial != 0:
                print(f"{c}{n}")
                total += 1
                
        else:
            new = dial + n
            if new >= 100 and dial != 0: 
                print(f"{c}{n}")
                total += 1
        dial = new % 100
    print(total)