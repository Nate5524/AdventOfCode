with open("4.txt", "r") as file:
    total = 0
    for line in file:
        line = line.split(":")[1]
        success,actual=[side.split() for side in line.split("|")]
        temp = 0
        for num in actual:
            if num in success:
                if temp == 0:
                    temp = 1
                else:
                    temp *= 2
        total += temp
    print(total)