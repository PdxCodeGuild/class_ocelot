




print(list('hello world'))





fruits = ['apple', 'banana', 'pear']
for i in range(100):
    k = i
    while k > len(fruits):
        k -= len(fruits)
    print(f'{i}%3={i%3} {fruits[k]}')











