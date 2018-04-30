from turtle import *

acolor = 0
speed(0)
grow = 4
edge_length = 20
i = 0

lColors = ['Red', 'Green', 'Blue', 'Yellow', 'purple', 'Orange']

while i < 200:
    forward(edge_length)
    right(170)
    edge_length = edge_length + grow
    if (i % 20) == 0:
        color(acolor)
        acolor += 1
        grow *= -1
    i = i + 1

left(90)
forward(100)

done()