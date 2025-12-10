import itertools


with open("9.txt", "r") as file:
    ls = [l.strip().split(",") for l in file]
    pts = [(int(x), int(y)) for x, y in ls]
    pairs = itertools.combinations(pts, 2)
    best = 0
    for pair in pairs:
        (x1, y1), (x2, y2) = pair
        a = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        best = max(best, a)
    print(best)
