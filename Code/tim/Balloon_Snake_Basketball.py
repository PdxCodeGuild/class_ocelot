import graphics
import math
import time as sleeper
import random


class Balls:

    def __init__(self, win, ball, r):
        self.ball = ball
        self.cir = graphics.Circle(graphics.Point(ball.getX(), ball.getY()), r)
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

    def update(self, time, w):
        self.xpos += time * self.xvel
        yvel1 = self.yvel0 - 32.174 * time
        self.ypos += time * (self.yvel0 + yvel1) / 2.0
        self.yvel0 = yvel1 * .99
        if self.xpos > w:
            self.reset_x()
        if self.ypos < 0:
            self.bounce()

    def bounce(self):
        self.yvel0 = abs(self.yvel0)
        self.ypos = 0.0
        self.yvel0 *= .95

    def getY(self): # didn't work with name "get_y"?
        return self.ypos

    def getX(self): # didn't work with name "get_x"?
        return self.xpos

    def reset_x(self):
        self.xpos = 0.0


class Floater:

    def __init__(self, x, y, xv, yv):
        self.xpos = x
        self.ypos = y
        self.xvel = xv
        self.yvel0 = yv

    def update(self, time, w):
        self.xpos += time * self.xvel
        yvel1 = self.yvel0 - 32.174 * time
        self.ypos += time * (self.yvel0 + yvel1) / 2.0
        self.yvel0 += 32.174 * time
        if self.xpos > w:
            self.reset_x()
        if self.ypos < 0:
            self.bounce()

    def bounce(self):
        self.yvel0 = abs(self.yvel0)
        self.ypos = 0.0

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

    def reset_x(self):
        self.xpos = 0.0


class Target:

    def __init__(self, win, r, h, diff):
        self.center = r - diff // 2
        self.ov = graphics.Oval(graphics.Point(r - diff, h), graphics.Point(r, h + 5))
        self.ov.draw(win)

    def check_floater(self, x, diff):
        if self.center - diff // 2 < x < self.center + diff // 2:
            return True
        return False

    def change(self, w, diff):
        m = random.randrange(w // 4)
        if self.center + m < w - diff // 2:
            self.center += m
            self.ov.move(m, 0)
        else:
            self.center -= m
            self.ov.move(-m, 0)


def get_inputs():
    diff = int(input('What difficulty level?\n > '))
    if diff == 1:
        diff = 54
    elif diff == 2:
        diff = 44
    elif diff == 3:
        diff = 36
    elif diff == 4:
        diff = 30
    else:
        diff = 24
    ang = float(input('What launch angle (in degrees, 1 to 90)?\n > '))
    a = int(input('What launch speed (1 to 5, 5 = fastest)?\n > '))
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
    a = int(input('How compact (1 to 5, 5 = most compact)?\n > '))
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
    return diff, ang, vel, freq, hei, time


def main():
    w = 1500
    h = 600
    diff, ang, vel, freq, hei, time = get_inputs()
    win = graphics.GraphWin('BALLOON SNAKE BASKETBALL', w, h)
    win.setCoords(0, 0, w, h)
    tar = Target(win, random.randrange(w // 2, w) - 10, h - 5, diff)
    b_ct = 0
    f_ct = 0
    score = 0
    b_balls = []
    f_balls = []
    while True:
        sleeper.sleep(.05)
        b_ct += 1
        if b_ct % freq == 1 and len(b_balls) + f_ct < 10:
            b = Bouncy(ang, vel, hei)
            t = Balls(win, b, 2)
            b_balls.append([b, t])
        if len(win.checkKey()) > 0:
            b = Floater(b_balls[0][0].getX(), b_balls[0][0].getY(), b_balls[0][0].xvel, b_balls[0][0].yvel0)
            t = Balls(win, b, 5)
            f_balls.append([b, t])
            b_balls[0][1].delete()
            b_balls.remove(b_balls[0])
            f_ct += 1
        for b in b_balls:
            b[0].update(time, w)
            b[1].update()
        for f in f_balls:
            f[0].update(time, w)
            f[1].update()
            if f[0].getY() > h - 5:
                if tar.check_floater(f[0].getX(), diff):
                    score += 1
                    tar.change(w, diff)
                f[1].delete()
                f_balls.remove(f)
                if f_ct == 10 and len(f_balls) == 0:
                    return(score)


score = main()
print(f'You got a {score}')
