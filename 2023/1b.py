def findSubstNum(str, start):
    if start >= len(str) - 2:
        return -1
    comp = str[start:start+3]
    if comp == "one":
        return 1
    elif comp == "two":
        return 2
    elif comp == "six":
        return 6
    
    if start >= len(str) - 3:
        return -1
    comp = str[start:start+4]
    if comp == "four":
        return 4
    elif comp == "five":
        return 5
    elif comp == "nine":
        return 9

    if start >= len(str) - 4:
        return -1
    comp = str[start:start+5]
    if comp == "three":
        return 3
    elif comp == "seven":
        return 7
    elif comp == "eight":
        return 8
    
    return -1

with open("1.txt", "r") as file:
    sum = 0
    for line in file:
        lineNum = ""
        for i in range(len(line)):
            f = findSubstNum(line,i)
            if line[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                lineNum += line[i]
            elif f != -1:
                lineNum += str(f)
        sum += int(lineNum[0]+lineNum[-1])
    print(sum)