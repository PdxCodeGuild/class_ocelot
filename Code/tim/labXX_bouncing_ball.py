import graphics
import math
import time as sleeper

class Tracker:

    def __init__(self, win, bncy):
        self.bncy = bncy
        self.cir = graphics.Circle(graphics.Point(bncy.getX(), bncy.getY()), 2)
        self.cir.draw(win)

    def update(self):
        p = self.cir.getCenter()
        x = p.getX()
        y = p.getY()
        self.cir.move(self.bncy.getX() - x, self.bncy.getY() - y)


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

    def getY(self): # didn't work with name "get_y"?
        return self.ypos

    def getX(self): # didn't work with name "get_x"?
        return self.xpos

    def reset_x(self):
        self.xpos = 0.0


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
    f_balls = []
    while b_ct / freq < balls + 100:
        sleeper.sleep(.05)
        b_ct += 1
        if b_ct % freq == 1 and len(f_balls) < balls:
            b = Bouncy(ang, vel, hei)
            t = Tracker(win, b)
            f_balls.append([b, t])
        for b in f_balls:
            b[0].update(time)
            if b[0].getY() < 0:
                b[0].bounce()
            if b[0].getX() > 1500:
                b[0].reset_x()
            b[1].update()
main()
