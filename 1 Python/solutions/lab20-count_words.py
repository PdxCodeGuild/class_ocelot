

with open('the_clue_of_the_golden_coin.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

lines = contents.split('\n')
for line in lines:
    print(line)

