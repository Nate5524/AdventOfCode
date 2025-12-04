RED = 12
GREEN = 13
BLUE = 14

def isPossible(case):
    case = case.split()
    for i in range(0,len(case),2):
        if case[i+1][0]== "r" and int(case[i]) > RED:
            return False
        if case[i+1][0]== "g" and int(case[i]) > GREEN:
            return False
        if case[i+1][0]== "b" and int(case[i]) > BLUE:
            return False
    return True


with open("2.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.split(":")
        linePossible = True
        for case in line[1].split(";"):
            if not isPossible(case):
                linePossible = False
        if linePossible:
            sum += int(line[0].split()[1])
    print(sum)