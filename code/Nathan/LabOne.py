from turtle import *

speed(0)
fillcolor('brown')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(50)
left(90)
end_fill()
forward(150)
fillcolor('yellow')

i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1
right(180)
forward(25)
right(90)
forward(125)
penup()
right(180)
forward(125)
right(90)
forward(100)
right(180)
right(90)
pendown()
forward(200)
i=0
while i < 360:
    forward(1)
    right(1)
    i = i + 1

left(180)
forward(200)
i=0
while i < 360:
    forward(1)
    left(1)
    i = i + 1


done()