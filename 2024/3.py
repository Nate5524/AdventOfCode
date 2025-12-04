with open("3.txt", "r") as file:
    for line in file:
        total = 0
        line = line.lower()
        for i in range(len(line)-7):
            if (line[i] == "m" 
                and line[i+1] == "u" 
                and line[i+2] == "l" 
                and line[i+3] == "("):
                
                a = ""
                off = 4
                og = off
                while line[i+off] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    a += line[i+off]
                    off += 1
                    if off > og + 3: continue
                print(f"a:{a}")
                if not (0 < len(a) <= 3 and line[i+off] == ","): continue
                off += 1
                b = ""
                og = off
                while line[i+off] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    b += line[i+off]
                    off += 1
                    if off > og + 3: continue
                print(f"b:{b}")
                if not (0 < len(b) <= 3 and line[i+off] == ")"): continue
                total += int(a) * int(b)
    print(total)
                