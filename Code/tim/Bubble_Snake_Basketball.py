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
        yvel1 = self.yvel0 - 50 * time
        self.ypos += time * (self.yvel0 + yvel1) / 2.0
        self.yvel0 = yvel1
        if self.xpos > w:
            self.reset_left()
        elif self.xpos < 0:
            self.reset_right(w)
        if self.ypos < 0:
            self.bounce()
            return True

    def go_right(self):
        self.xvel = abs(self.xvel)

    def go_left(self):
        self.xvel = -abs(self.xvel)

    def jump(self, ang, vel):
        theta = math.radians(ang)
        self.yvel0 = vel * math.sin(theta)

    def bounce(self):
        self.yvel0 = abs(self.yvel0)
        self.ypos = 0.0
        self.yvel0 *= .95

    def flutter(self, vel):
        self.yvel0 = vel * .3

    def getY(self): # didn't work with name "get_y"?
        return self.ypos

    def getX(self): # didn't work with name "get_x"?
        return self.xpos

    def reset_left(self):
        self.xpos = 0.0

    def reset_right(self, w):
        self.xpos = w


class Floater:

    def __init__(self, x, y, xv, yv):
        self.xpos = x
        self.ypos = y
        self.xvel = xv
        self.yvel0 = yv

    def update(self, time, w):
        self.xpos += time * self.xvel
        yvel1 = self.yvel0 + 50 * time
        self.ypos += time * (self.yvel0 + yvel1) / 2.0
        self.yvel0 = yvel1
        self.xvel *= .95
        if self.xpos > w:
            self.reset_left()
        elif self.xpos < 0:
            self.reset_right(w)
        if self.ypos < 0:
            self.bounce()

    def bounce(self):
        self.yvel0 = abs(self.yvel0)
        self.ypos = 0.0

    def blow(self):
        self.yvel0 -= 20
        self.xvel += 1

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

    def reset_left(self):
        self.xpos = 0.0

    def reset_right(self, w):
        self.xpos = w


class Target:

    def __init__(self, win, r, h, tar_wid, tar_max_vel, tar_acc):
        self.center = r - tar_wid // 2
        self.ov = graphics.Oval(graphics.Point(r - tar_wid, h), graphics.Point(r, h + 5))
        self.ov.draw(win)
        self.max_vel = tar_max_vel
        self.acc = tar_acc
        self.xvel0 = 0.0

    def check_floater(self, x, tar_wid):
        if self.center - tar_wid // 2 - 1 <= x <= self.center + tar_wid // 2 + 1:
            return True
        return False

    def new_target(self, r):
        self.ov.move(r, 0)
        self.center += r
        self.xvel0 = 0.0

    def move(self, time, x, w):
        if self.center >= x:
            if x - self.center < 500:
                xvel1 = min(self.xvel0 + self.acc, self.max_vel)
            else:
                xvel1 = self.xvel0
            self.ov.move(time * (self.xvel0 + xvel1) / 2, 0)
            self.center += time * (self.xvel0 + xvel1) / 2
            self.xvel0 = xvel1
        else:
            if self.center - x < 500:
                xvel1 = max(self.xvel0 - self.acc, -self.max_vel)
            else:
                xvel1 = self.xvel0
            self.ov.move(time * (self.xvel0 + xvel1) / 2, 0)
            self.center += time * (self.xvel0 + xvel1) / 2
            self.xvel0 = xvel1
        if self.center > w:
            return 'over'
        elif self.center < 0:
            return 'under'

def get_inputs():
    a = int(input('What difficulty level?\n > '))
    if a == 1:
        tar_wid = 80
        tar_max_vel = 0
        tar_acc = 0
    elif a == 2:
        tar_wid = 70
        tar_max_vel = 6
        tar_acc = 1
    elif a == 3:
        tar_wid = 60
        tar_max_vel = 12
        tar_acc = 1.5
    elif a == 4:
        tar_wid = 50
        tar_max_vel = 18
        tar_acc = 1.8
    else:
        tar_wid = 40
        tar_max_vel = 24
        tar_acc = 2
    ang = 60
    vel = 260
    freq = 2
    hei = 0
    time = .1
    return tar_wid, tar_max_vel, tar_acc, ang, vel, freq, hei, time


def main():
    w = 1500
    h = 600
    tar_wid, tar_max_vel, tar_acc, ang, vel, freq, hei, time = get_inputs()
    win = graphics.GraphWin('BUBBLE SNAKE BASKETBALL', w, h)
    win.setCoords(0, 0, w, h)
    tar = Target(win, random.randrange(w // 2, w) - 10, h - 5, tar_wid, tar_max_vel, tar_acc)
    b_ct = 0
    f_ct = 0
    h_ct = 0
    score = 0
    fx = 0
    l_ck = ''
    turn = -1
    changing = False
    b_balls = []
    f_balls = []
    while True:
        sleeper.sleep(.05)
        b_ct += 1
        if b_ct % freq == 1 and len(b_balls) + f_ct < 10:
            b = Bouncy(ang, vel, hei)
            t = Balls(win, b, 2)
            b_balls.append([b, t, 0])
        ck = win.checkKey()
        if ck == l_ck:
            h_ct += 1
        if ck != '' and not changing:
            turn = 0
            if ck == 'Right':
                for b in b_balls:
                    b[2] = 1
            elif ck == 'Left':
                for b in b_balls:
                    b[2] = 2
            elif ck == 'Up':
                if h_ct < 3:
                    for b in b_balls:
                        b[2] = 3
                else:
                    for b in b_balls:
                        b[2] = 4
            elif ck == 'Down':
                for f in f_balls:
                    f[0].blow()
        else:
            h_ct = 0
        if ck == 'space':
            b = Floater(b_balls[0][0].getX(), b_balls[0][0].getY(), b_balls[0][0].xvel, b_balls[0][0].yvel0)
            t = Balls(win, b, 5)
            f_balls.append([b, t])
            b_balls[0][1].delete()
            b_balls.remove(b_balls[0])
            f_ct += 1
            if changing:
                turn -= 1
        l_ck = ck
        for b in b_balls:
            j = b[0].update(time, w)
            if j and b[2] != 0 and b_balls.index(b) == turn:
                turn += 1
                if b == b_balls[0]:
                    changing = True
                if b == b_balls[-1]:
                    changing = False
                    turn = -1
                if b[2] == 1:
                    b[0].go_right()
                elif b[2] == 2:
                    b[0].go_left()
                elif b[2] == 3:
                    b[0].jump(ang, vel)
                b[2] = 0
            elif b[2] == 4 and b_balls.index(b) == turn:
                if b == b_balls[0]:
                    changing = True
                    fx = b[0].getX()
                if b[0].xvel > 0 and b[0].getX() >= fx:
                    b[0].flutter(vel)
                    b[2] = 0
                    turn += 1
                    if b == b_balls[-1]:
                        changing = False
                        turn = -1
                        fx = 0
                elif b[0].xvel < 0 and b[0].getX() <= fx:
                    b[0].flutter(vel)
                    b[2] = 0
                    turn += 1
                    if b == b_balls[-1]:
                        changing = False
                        turn = -1
                        fx = 0
            b[1].update()
        for f in f_balls:
            f[0].update(time, w)
            f[1].update()
            if f[0].getY() > h - 5:
                if tar.check_floater(f[0].getX(), tar_wid):
                    score += 1
                    tar.new_target(random.randrange(0, w // 2))
                f[1].delete()
                f_balls.remove(f)
                if f_ct == 10 and len(f_balls) == 0:
                    return(score)
        if len(b_balls) > 0:
            x = b_balls[0][0].getX()
        else:
            x = w // 2
        t = tar.move(time, x, w)
        if t == 'over':
            tar.new_target(-random.randrange(tar_wid + 10, w - 10))
        elif t == 'under':
            tar.new_target(random.randrange(tar_wid + 10, w - 10))

score = main()
print(f'You got a {score}')

