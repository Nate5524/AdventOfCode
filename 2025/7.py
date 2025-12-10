g = []
with open("7.txt", "r") as file:
    g = [l.strip() for l in file]
f = [(1, g[0].index("S"))]
s = set()
t = 0
while len(f) > 0:
    r, c = f.pop()
    if r >= len(g) or c >= len(g[r]) or (r, c) in s:
        continue
    s.add((r, c))
    if g[r][c] == ".":
        f.append((r + 1, c))
    else:
        f.append((r, c + 1))
        f.append((r, c - 1))
        t += 1
print(t)
