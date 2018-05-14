from turtle import *

edge_length = 0
i = 0
while i < 36:
    forward(edge_length)
    right(360/8)
    i = i + 1
    edge_length = edge_length + 1



forward((edge_length-1)/2)
left(90)
forward(100)

right(135)
forward(50)
back(50)
right(90)
forward(50)

left(30)
forward(5)
right(90)
forward(5)
back(10)
forward(5)
left(90)
forward(40)
back(45)
right(30)
back(50)
right(135)

forward(100)
left(45)
forward(50)
back(50)
right(90)
forward(50)
back(50)

done()