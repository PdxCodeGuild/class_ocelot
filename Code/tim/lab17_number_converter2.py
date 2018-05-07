
numerals = [['M', 1000], ['D', 500], ['C', 100], ['L', 50], ['X', 10], ['V', 5], ['I', 1]]

while True:
    num = int(input('What number do you want to translate into Roman Numerals?\n > '))
    rom = ''
    for i in range(len(numerals)):
        print(num, numerals[i][1])
        if numerals[i][1] - 3 <= num <= numerals[i][1]:
            rom += 'I' * (numerals[i][1] - num) + numerals[i][0]
            break
        elif 7 <= num <= 9:
            rom += 'I' * (10 - num) + 'X'
            break
        else:
            t = num // numerals[i][1]
            if t > 0:
                rom += numerals[i][0] * t
                num -= t * numerals[i][1]
    print(rom)
