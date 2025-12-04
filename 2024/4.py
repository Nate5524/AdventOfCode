with open("4.txt", "r") as file:
    grid = [line for line in file]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0<= i + di*3 < len(grid) and 0 <= j+dj*3<len(grid[0]) and grid[i+di][j+dj] == "M" and grid[i+di*2][j+dj*2] == "A" and grid[i+di*3][j+dj*3] == "S": total += 1
    print(total)