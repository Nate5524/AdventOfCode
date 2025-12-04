with open("1.txt", "r") as file:
    sum = 0
    for line in file:
        lineNum = ""
        for char in line:
            if char in ["0","1","2","3","4","5","6","7","8","9"]:
                lineNum += char
        sum += int(lineNum[0]+lineNum[-1])
    print(sum)