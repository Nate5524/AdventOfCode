with open("2.txt", "r") as file:
    x = [x for x in file.read().splitlines()]
    ans = 0
    for pair in x:
        if pair[0] == 'A':
            if pair[2] == 'X': y = 'Z'
            elif pair[2] == 'Y': y = 'X'
            elif pair[2] == 'Z': y = 'Y'
        elif pair[0] == 'B':
            if pair[2] == 'X': y = 'X'
            elif pair[2] == 'Y': y = 'Y' 
            elif pair[2] == 'Z': y = 'Z'
        elif pair[0] == 'C':
            if pair[2] == 'X': y = 'Y'
            elif pair[2] == 'Y': y = 'Z'
            elif pair[2] == 'Z': y = 'X'
            
        if pair[0] == 'A':
            if y == 'X': ans += 4
            elif y == 'Y': ans += 8
            elif y == 'Z': ans += 3
        elif pair[0] == 'B':
            if y == 'X': ans += 1
            elif y == 'Y': ans += 5
            elif y == 'Z': ans += 9
        elif pair[0] == 'C':
            if y == 'X': ans += 7
            elif y == 'Y': ans += 2
            elif y == 'Z': ans += 6
    print(ans)
