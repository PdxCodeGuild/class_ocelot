

with open('goldencoin.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

lines = contents.split('\n')
for line in lines:
    print(line)

