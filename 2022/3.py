with open('3.txt', 'r') as file:
    x = [x for x in file.read().splitlines()]
    ans = 0
    for pack in x:
        half1 = pack[:len(pack) // 2]
        half2 = pack[len(pack) // 2:]
        lhalf1 = []
        lhalf2 = []
        for i in range(len(half1)):
            lhalf1.append(ord(half1[i]))
            lhalf2.append(ord(half2[i]))
        for j in range(len(lhalf1)):
            if 97 <= lhalf1[j] <= 122:
                lhalf1[j] -= 96
            elif 65 <= lhalf1[j] <= 90:
                lhalf1[j] -= 38
            if 97 <= lhalf2[j] <= 122:
                lhalf2[j] -= 96
            elif 65 <= lhalf2[j] <= 90:
                lhalf2[j] -= 38
            used = []
        for num in lhalf1:
            if num in lhalf2:
                if num not in used:
                    used.append(num)
                    ans += num
    print(ans)
