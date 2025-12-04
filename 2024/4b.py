with open("4.txt", "r") as file:
    grid = [line for line in file]
    total = 0
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if grid[i][j] == "A":
                x = [grid[i-1][j-1], grid[i-1][j+1], grid[i+1][j-1], grid[i+1][j+1]]
                if x.count("M") == 2 and x.count("S") == 2 and x[0] != x[3]: total += 1
    print(total)