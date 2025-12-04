import re


filt = "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
with open("3.txt", "r") as file:
    total = 0
    doing = True
    for line in file:
        matches = re.findall(filt, line)
        for match in matches:
            if re.match("do\(\)", match) != None: doing = True
            elif re.match("don't\(\)", match) != None: doing = False
            elif doing:
                m = re.split("mul\(|,|\)", match)
                total += int(m[1]) * int(m[2])
    print(total)