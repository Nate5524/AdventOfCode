with open("1.txt", "r") as file:
    x = [int(x) if x != '' else '' for x in file.read().splitlines()]
    print(x)
    i = 0
    ans = []
    for num in range(len(x)):
        if x[num] == '':
            ans.append(sum(x[i:num]))
            i = num + 1
    print(ans.pop(ans.index(max(ans))))
    print(ans.pop(ans.index(max(ans))))
    print(ans.pop(ans.index(max(ans))))