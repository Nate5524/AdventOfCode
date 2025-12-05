import re

with open("./2015/5.txt", "r") as file:
    t=0
    r = re.compile(r"(?=.*(..).*\1)(?=.*(.).\2)")
    for line in file:
        if re.search(r,line.strip()):
            t+=1
    print(t)