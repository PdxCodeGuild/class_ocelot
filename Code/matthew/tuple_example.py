







point = (5, 2, 4.5, (), [], {})
print(point[0])
#point[0] = 6

point[4].append('hello world')
print(point)



for element in point:
    print(element)



print(list(range(10)))

print(range(10))







fruits = ['apple', 'banana', 'pear']
for i in range(len(fruits)):
    #print(f'{i} {fruits[i]}')
    fruits[i] += '!'



for fruit in fruits:
    fruit += '!'


lists = [[1], [2], [3]]

for list in lists:
    list.append(4)

print(lists)




a = 5
b = a
b = b + 1
print(a)



print(fruits)




