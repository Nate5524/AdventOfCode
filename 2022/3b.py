with open('3.txt', 'r') as file:
    x = [x for x in file.read().splitlines()]
    ans = 0
    for i in range(0, len(x), 3):
        elf1, elf2, elf3 = x[i], x[i + 1], x[i + 2]
        for letter in elf1:
            if letter in elf2 and letter in elf3:
                letter = ord(letter)
                if 97 <= letter <= 122:
                    ans += letter - 96
                    break
                elif 65 <= letter <= 90:
                    ans += letter - 38
                    break
    print(ans)

