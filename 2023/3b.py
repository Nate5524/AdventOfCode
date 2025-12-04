with open("3.txt", "r") as file:
    lineReps = []
    numsList = []
    # put data into a useable format. Each "char" is either None (a "."), "*" (a part of some kind), 
    # or a pointer to an integer in the numsList - allows for setLike behavior with some repetition at sum step

    # Added new representation for part 2: "#" is now used to represent gears
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
            elif char == "*":
                for i in range(len(tempNum)):
                    lineRep.append(len(numsList))
                if tempNum != "":
                    numsList.append(tempNum)
                tempNum = ""
                lineRep.append("#")
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

    # Part 2: search based upon gears rather than all parts.
    # Find the ones that have exactly 2 number neighbors and sum the product of those two numbers
    total = 0
    for line in range(len(lineReps)):
        for char in range(len(lineReps[line])):
            if lineReps[line][char] == "#":
                # an even funkier 3x3 search function
                neighbors = []
                # check for valid neighboring nums (plus some weirdness to avoid nums that take up multiple neighboring tiles)
                
                #check line above gear
                if line-1 >= 0 and lineReps[line-1][char] not in [None, "*", "#"]:
                    hCenterNum = lineReps[line-1][char]
                    neighbors.append(hCenterNum)
                else:
                    hCenterNum = -1
                if char-1>=0 and hCenterNum != lineReps[line-1][char-1] and lineReps[line-1][char-1] not in [None, "*", "#"]:
                    neighbors.append(lineReps[line-1][char-1])
                if char+1<= len(lineReps[line+1]) and hCenterNum != lineReps[line-1][char+1] and lineReps[line-1][char+1] not in [None, "*", "#"]:
                    neighbors.append(lineReps[line-1][char+1])

                #check line below gear
                if line+1 <= len(lineReps) and lineReps[line+1][char] not in [None, "*", "#"]:
                    hCenterNum = lineReps[line+1][char]
                    neighbors.append(hCenterNum)
                else: 
                    hCenterNum = -1
                if char-1>=0 and hCenterNum != lineReps[line+1][char-1] and lineReps[line+1][char-1] not in [None, "*", "#"]:
                    neighbors.append(lineReps[line+1][char-1])
                if char+1<= len(lineReps[line+1]) and hCenterNum != lineReps[line+1][char+1] and lineReps[line+1][char+1] not in [None, "*", "#"]:
                    neighbors.append(lineReps[line+1][char+1])

                #check line of gear
                if char-1>=0 and lineReps[line][char-1] not in [None, "*", "#"]:
                    neighbors.append(lineReps[line][char-1])
                if char+1<= len(lineReps[line+1]) and lineReps[line][char+1] not in [None, "*", "#"]:
                    neighbors.append(lineReps[line][char+1])
                # print(neighbors)
                if len(neighbors) == 2:
                    total += int(numsList[neighbors[0]])*int(numsList[neighbors[1]])
                    # print(total)
    print(total)
    # print(sum(range(1000)))