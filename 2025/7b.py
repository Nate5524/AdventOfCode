g = []
with open("7.txt", "r") as file:
    g = [l.strip() for l in file]
C, R = len(g[0]), len(g)

memo = [[None] * C for _ in range(R)]
memo[R - 1] = [1] * C


def solve(r, c):
    if memo[r][c] != None:
        return memo[r][c]
    if g[r][c] == ".":
        memo[r][c] = solve(r + 1, c)
    else:
        memo[r][c] = solve(r, c + 1) + solve(r, c - 1)
    return memo[r][c]


print(solve(1, g[0].index("S")))