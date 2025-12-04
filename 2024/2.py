with open("2.txt", "r") as file:
    safe = 0
    for line in file:
        l = line.split()
        prev = int(l[0])
        ok = True
        asc = -1 # 0 desc, 1 asc
        for i in range(1, len(l)):
            cur = int(l[i])
            if abs(cur - prev) > 3:
                ok = False
                break
            if asc == -1:
                if prev < cur:
                    asc = 1
                elif prev > cur:
                    asc = 0
                else:
                    ok = False
                    break
            else:
                if asc == 0 and prev <= cur:
                    ok = False
                    break
                if asc == 1 and cur <= prev:
                    ok = False
                    break
            prev = cur
        if ok: safe += 1
    print(safe)