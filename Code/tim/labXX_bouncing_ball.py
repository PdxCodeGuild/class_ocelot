import graphics
import math
import time as sleeper

class Tracker:

    def __init__(self, win, obj):
        self.obj = obj
        self.cir = graphics.Circle(graphics.Point(obj.getX(), obj.getY()), 2)
        self.cir.draw(win)

    def update(self):
        p = self.cir.getCenter()
        x = p.getX()
        y = p.getY()
        self.cir.move(self.obj.getX() - x, self.obj.getY() - y)

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
        self.yvel0 = yvel1 * .98

    def bounce(self):
        self.yvel0 *= -1
        self.ypos = 0.0

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

    def resetX(self):
        self.xpos = 0.0

def getInputs():
    ang = float(input('How high do you want to kick the ball (in degrees, 1 to 90)? > '))
    hard = int(input('How hard do you want to kick the ball (1 to 5, 5 = hardest)? > '))
    if hard == 1:
        vel = 50
    elif hard == 2:
        vel = 100
    elif hard == 3:
        vel = 150
    elif hard == 4:
        vel = 200
    else:
        vel = 250
    hei = 0
    time = .1
    return ang, vel, hei, time

def main():
    ang, vel, hei, time = getInputs()

    win = graphics.GraphWin('Bouncy bouncy bouncy...', 1500, 500)
    win.setCoords(0, 0, 1500, 500)

    b_ball = Bouncy(ang, vel, hei)
    t = Tracker(win, b_ball)
    while b_ball.getX() < 1500:
        sleeper.sleep(.05)
        b_ball.update(time)
        if b_ball.getY() < 0:
            b_ball.bounce()
        if b_ball.getX() > 1500:
            b_ball.resetX()
        t.update()

main()