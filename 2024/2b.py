with open("2.txt", "r") as file:
    safe = 0
    for line in file:
        l = line.split()
        prev = int(l[0])
        ok = 0
        asc = -1 # 0 desc, 1 asc
        for i in range(1, len(l)):
            cur = int(l[i])
            if abs(cur - prev) > 3:
                ok += 1
            if asc == -1:
                if prev < cur:
                    asc = 1
                elif prev > cur:
                    asc = 0
                else:
                    ok += 1
            else:
                if asc == 0 and prev <= cur:
                    ok += 1
                if asc == 1 and cur <= prev:
                    ok += 1
            prev = cur
        if ok <= 1: safe += 1
    print(safe)