with open("6.txt", "r") as file:
    g = []
    for line in file:
        g.append(list(line.strip()))
    r = -1
    c = -1
    d = 0
    for i in range(len(g)):
        if "^" in g[i]:
            r = i
            c = g[i].index("^")
            break
    rm = r
    cm = c
    
    visited = []
    
    for dr in range(len(g)):
        for dc in range(len(g[dr])):
            change = g[dr][dc] != "#"
            if change: g[dr][dc] = "#"
            r = rm
            c = cm
            
            total = 0
            
            minlen = float("inf")
            minct = 0
            loop = False
            iters = 0
            while True:
                if g[r][c] == "X": total += 1
                else: g[r][c] = "X"
                iters += 1
                print(iters, total)
                
                if d == 0:
                    r -= 1
                    if 0 <= r < len(g) and 0 <= c < len(g[0]):
                        if g[r][c] == "#":
                            d = 1
                            r += 1
                            visited.append((r,c,d))
                    else:
                        break
                elif d == 1:
                    c += 1
                    if 0 <= r < len(g) and 0 <= c < len(g[0]):
                        if g[r][c] == "#":
                            d = 2
                            c -= 1
                            visited.append((r,c,d))
                    else:
                        break
                elif d == 2:
                    r += 1
                    if 0 <= r < len(g) and 0 <= c < len(g[0]):
                        if g[r][c] == "#":
                            d = 3
                            r -= 1
                            visited.append((r,c,d))
                    else:
                        break
                else:
                    c -= 1
                    if 0 <= r < len(g) and 0 <= c < len(g[0]):
                        if g[r][c] == "#":
                            d = 0
                            c += 1
                            visited.append((r,c,d))
                    else:
                        break
                for v in visited:
                    if r == v[0] and c == v[1] and d == v[2]:
                        loop = True
                        break
            
            for i in range(len(g)):
                for j in range(len(g[i])):
                    if g[i][j] == "X":
                        # total += 1
                        g[i][j] = "."
            
            if change: g[dr][dc] = "."
            if not loop: continue 
            
            
            if total < minlen: minct = 1
            elif total == minlen: minct += 1
    print(minct)