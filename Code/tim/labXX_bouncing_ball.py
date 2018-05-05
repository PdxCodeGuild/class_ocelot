import graphics
import math
import time as sleeper
import pygame
import random

class Tracker:

    def __init__(self, win, ball):
        self.ball = ball
        self.cir = graphics.Circle(graphics.Point(ball.getX(), ball.getY()), 2)
        self.cir.draw(win)

    def update(self):
        p = self.cir.getCenter()
        x = p.getX()
        y = p.getY()
        self.cir.move(self.ball.getX() - x, self.ball.getY() - y)

    def delete(self):
        self.cir.undraw()

class Bouncy:

    def __init__(self, ang, vel, hei):
        self.xpos = 0.0
        self.ypos = hei
        theta = math.radians(ang)
        self.xvel = vel * math.cos(theta)
        self.yvel0 = vel * math.sin(theta)

    def update(self, time):
        self.xpos += time * self.xvel
        yvel1 = self.yvel0 - 32.174 * time
        self.ypos += time * (self.yvel0 + yvel1) / 2.0
        self.yvel0 = yvel1 * .99

    def bounce(self):
        self.yvel0 *= -1
        self.ypos = 0.0
        self.yvel0 *= .95

    def getY(self): # didn't work with name "get_y"?
        return self.ypos

    def getX(self): # didn't work with name "get_x"?
        return self.xpos

    def reset_x(self):
        self.xpos = 0.0


class Floater:

    def __init__(self, x, y, v):
        self.xpos = x
        self.ypos = y
        self.vel = v

    def update(self, time):
        self.ypos += time * self.vel
        self.vel *= 1.2

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos


def get_inputs():
    balls = int(input('How many balls do you want to launch? > '))
    ang = float(input('What launch angle (in degrees, 1 to 90)? > '))
    a = int(input('How hard (1 to 5, 5 = hardest)? > '))
    if a == 1:
        vel = 150
    elif a == 2:
        vel = 180
    elif a == 3:
        vel = 210
    elif a == 4:
        vel = 240
    else:
        vel = 270
    a = int(input('How frequently (1 to 5, 5 = fastest)? > '))
    if a == 1:
        freq = 30
    elif a == 2:
        freq = 20
    elif a == 3:
        freq = 12
    elif a == 4:
        freq = 6
    else:
        freq = 3
    hei = 0
    time = .1
    return balls, ang, vel, freq, hei, time


def main():
    balls, ang, vel, freq, hei, time = get_inputs()
    win = graphics.GraphWin('Bouncy bouncy bouncy...', 1500, 600)
    win.setCoords(0, 0, 1500, 600)
    b_ct = 0
    f_ct = 0
    b_balls = []
    f_balls = []
    while b_ct / freq < balls + 200:
        sleeper.sleep(.05)
        b_ct += 1
        if b_ct % freq == 1 and len(b_balls) + f_ct < balls:
            b = Bouncy(ang, vel, hei)
            t = Tracker(win, b)
            b_balls.append([b, t])
        if len(win.checkKey()) > 0:
            r = random.randrange(len(b_balls))
            b = Floater(b_balls[r][0].getX(), b_balls[r][0].getY(), 20)
            t = Tracker(win, b)
            f_balls.append([b, t])
            b_balls[r][1].delete()
            b_balls.remove(b_balls[r])
            f_ct += 1
        for b in b_balls:
            b[0].update(time)
            if b[0].getY() < 0:
                b[0].bounce()
            if b[0].getX() > 1500:
                b[0].reset_x()
            b[1].update()
        for f in f_balls:
            f[0].update(time)
            if f[0].getY() > 1000:
                f_balls.remove(f)
                if f_ct == balls:
                    f[1].update()
                    exit()
            f[1].update()

main()
