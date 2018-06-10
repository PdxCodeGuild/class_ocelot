from turtle import *

color("red")

# head
circle(25)

# neck
seth(270)
forward(20)

# arms
arm_len = 35

# arm left
arm_angle_left = 110

right(arm_angle_left)
forward(arm_len)
left(180)
forward(arm_len)
seth(270)

# arm right
arm_angle_right = 20

left(arm_angle_right)
forward(arm_len)
left(180)
forward(arm_len)
seth(270)

# body
forward(40)

# legs
leg_len = 45
leg_angle = 25

# leg left
right(leg_angle)
forward(leg_len)
left(180)
forward(leg_len)
seth(270)

# leg right
left(leg_angle)
forward(leg_len)
left(180)
forward(leg_len)
seth(270)

done()
