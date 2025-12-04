with open("2.txt", "r") as file:
    x = [x for x in file.read().splitlines()]
    ans = 0
    for pair in x:
        if pair[0] == 'A':
            if pair[2] == 'X': ans += 4
            elif pair[2] == 'Y': ans += 8
            elif pair[2] == 'Z': ans += 3
        elif pair[0] == 'B':
            if pair[2] == 'X': ans += 1
            elif pair[2] == 'Y': ans += 5
            elif pair[2] == 'Z': ans += 9
        elif pair[0] == 'C':
            if pair[2] == 'X': ans += 7
            elif pair[2] == 'Y': ans += 2
            elif pair[2] == 'Z': ans += 6
    print(ans)