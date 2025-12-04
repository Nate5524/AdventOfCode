inp = input().split(",")
total = 0
for pair in inp:
    low,hi = pair.split("-")
    for v in range(int(low), int(hi)+1):
        s = str(v)
        chunk_size = 1
        while chunk_size <= len(s)//2:
            bad = True
            first = s[0:chunk_size]
            for d in range(chunk_size, len(s), chunk_size):
                if first != s[d:d+chunk_size]:
                    bad = False
                    break
            if bad:
                total += v
                break
            chunk_size += 1
            while len(s) % chunk_size != 0: chunk_size += 1
print(total)