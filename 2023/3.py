with open("3.txt", "r") as file:
    lineReps = []
    numsList = []
    # put data into a useable format. Each "char" is either None (a "."), "*" (a part of some kind), 
    # or a pointer to an integer in the numsList - allows for setLike behavior with some repetition at sum step
    for line in file:
        lineRep = []
        tempNum = ""
        for char in line:
            if char in ["0","1","2","3","4","5","6","7","8","9"]:
                tempNum += char
            elif char == ".":
                for i in range(len(tempNum)):
                    lineRep.append(len(numsList))
                if tempNum != "":
                    numsList.append(tempNum)
                tempNum = ""
                lineRep.append(None)
            elif char != "\n":
                for i in range(len(tempNum)):
                    lineRep.append(len(numsList))
                if tempNum != "":
                    numsList.append(tempNum)
                tempNum = ""
                lineRep.append("*")
        lineReps.append(lineRep)
        if tempNum != "":
            for i in range(len(tempNum)):
                lineRep.append(len(numsList))
            if tempNum != "":
                numsList.append(tempNum)
            tempNum = ""
    # print(lineReps) # uncomment to visualize the data grid

    # print("Length numsList"+str(len(numsList)))
    # print(numsList)
    
    # search each part for surrounding valid numbers, use them and then mark the number as used
    total = 0
    for line in range(len(lineReps)):
        for char in range(len(lineReps[line])):
            if lineReps[line][char] == "*":
                # basically a funky 3x3 search function
                for i in range(-1,2):
                    for j in range(-1,2):
                        if line+i >= 0 and line+i < len(lineReps) and char+j >= 0 and char+j < len(lineReps[line]):
                            if lineReps[line+i][char+j] not in [None, "*"]:
                                # print(lineReps[line+i][char+j])
                                total+=int(numsList[lineReps[line+i][char+j]])
                                numsList[lineReps[line+i][char+j]] = 0
                                # print(numsList)
    print(total)
    # print(sum(range(1000)))