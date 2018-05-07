
numerals = (('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1))

while True:
    num = int(input('What number do you want to translate into Roman Numerals?\n > '))
    rom = ''
    for i in range(len(numerals)):
        t = num // numerals[i][1]
        if t > 0:
            rom += numerals[i][0] * t
            num -= t * numerals[i][1]
        for j in range(i + 1, len(numerals)):
            print(num, numerals[i][1] - numerals[j][1])
            if num > (numerals[i][1] - numerals[j][1]) and num // (numerals[i][1] - numerals[j][1]) == 1:
                rom += numerals[j][0] + numerals[i][0]
                num -= numerals[i][1] - numerals[j][1]
                break
    print(rom)
