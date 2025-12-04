with open('4.txt', 'r') as file:
    x = [x.split(',') for x in file.read().splitlines()]
    ans = 0
    for pair in x:
        pair[0] = [int(x) for x in pair[0].split('-')]
        pair[1] = [int(x) for x in pair[1].split('-')]
        for num in range(pair[0][0], pair[0][1] + 1):
            if num in range(pair[1][0], pair[1][1] + 1):
                ans+= 1
                break
    print(ans)