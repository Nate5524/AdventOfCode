with open('4.txt', 'r') as file:
    x = [x.split(',') for x in file.read().splitlines()]
    ans = 0
    for pair in x:
        pair[0] = [int(x) for x in pair[0].split('-')]
        pair[1] = [int(x) for x in pair[1].split('-')]
        if pair[0][0] <= pair[1][0] <= pair[0][1] and pair[0][0] <= pair[1][1] <= pair[0][1]:
            ans +=1
        elif pair[1][0] <= pair[0][0] <= pair[1][1] and pair[1][0] <= pair[0][1] <= pair[1][1]:
            ans += 1
    print(ans)