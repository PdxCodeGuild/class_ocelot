from turtle import *

acolor = 0
speed(0)
grow = 4
edge_length = 20
i = 0

lColors = ['Red', 'Yellow', 'Green', 'Blue', 'purple', 'Orange']

while i < 200:
    forward(edge_length)
    right(170)
    edge_length = edge_length + grow
    if (i % 20) == 0:
        color(lColors[acolor])
        acolor += 1
        if acolor >= len(lColors):
            acolor = 0
    i = i + 1

left(90)
forward(100)

done()