with open("1.txt", "r") as file:
    s = file.readline().strip()
    print(s.count("(")-s.count(")"))