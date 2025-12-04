with open("4.txt", "r") as file:
    copyIndex = 0
    numLines = len(file.readlines())
    numCopies = [1]*numLines
    file.seek(0) # reset file pointer to beginning
    for line in file:
        line = line.split(":")[1]
        success,actual=[side.split() for side in line.split("|")]

        numSuccesses = 0
        for num in actual:
            if num in success:
                numSuccesses += 1
        # print("wins:"+str(numSuccesses))
        for i in range(1,numSuccesses+1):
            numCopies[copyIndex+i] += 1 * numCopies[copyIndex]
        copyIndex += 1
    print(sum(numCopies))