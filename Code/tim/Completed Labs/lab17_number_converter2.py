
numerals = (('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1))


def to_roman_numerals(num):
    rom = ''
    for i in range(len(numerals)):
        t = num // numerals[i][1]
        if t > 0:
            rom += numerals[i][0] * t
            num -= t * numerals[i][1]
        for j in range(i + 1, len(numerals)):
            if j == i + 1 and numerals[i][1] == numerals[j][1] * 2:
                continue
            if num >= (numerals[i][1] - numerals[j][1]):
                rom += numerals[j][0] + numerals[i][0]
                num -= numerals[i][1] - numerals[j][1]
                break
    return rom


for i in range(10):
    p_table = []
    for j in range(10):
        p_table.append(to_roman_numerals(i * 1 + j + 1))
    print(p_table)
