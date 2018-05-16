
import graphics as gr
import math
import time as sleeper
import random

time = .05

class Drawable:
    def __init__(self, x, y, wid, xvel=0, yvel0=0):
        self.xpos = x
        self.ypos = y
        self.rest_y = y
        self.xvel = xvel
        self.yvel0 = yvel0
        self.wid = wid


class Hero:
    def __init__(self, win):
        self.rest_y = 20
        self.state = None
        self.balls = []
        next_y_spot = 0
        size = 40
        for i in range(3):
            size *= .8
            next_y_spot += size / 2                         # Bottom half of current ball
            self.balls.append(Ball(200, next_y_spot, size, win))
            next_y_spot += size / 2                         # Top half of current ball


    def update(self, action, l_ct, ene, sce):
        if self.check_action():
            if action == 'down':
                if self.balls[0].ypos > self.rest_y:            # check to see if you're mid-air
                    for i in range(len(self.balls)):
                        self.balls[i].set_pound(i * 3 + l_ct)
                else:                       # otherwise crouch
                    for i in range(1, len(self.balls)):
                        self.balls[i].crouch(.2)
                    self.state = 'crouched'
            elif action == 'up':
                if self.balls[0].ypos > self.rest_y:            # check to see if you're mid-air
                    for i in range(len(self.balls) - 1, -1, -1):
                        self.balls[i].set_dbl_jump((len(self.balls) - i) * 3 + l_ct)    # set a staggered jump, the disconnected ball effect
                elif self.check_action():
                    for b in self.balls:                        # otherwise do a regular jump
                        b.jump()
        for i in range(len(self.balls)):                    # loop through the balls
            for j in range(len(self.balls[i].action)):      # loop through the actions for each ball
                if j >= len(self.balls[i].action):
                    continue
                if self.balls[i].action[j][1] == l_ct:
                    if self.balls[i].action[j][0] == 'dbl_jump':
                        self.balls[i].dbl_jump()
                        self.balls[i].action.remove(self.balls[i].action[j])
                    elif self.balls[i].action[j][0] == 'pound':
                        self.balls[i].pound()
                        self.balls[i].action.remove(self.balls[i].action[j])
            self.balls[i].update(ene, sce, i)

    def change_dir(self, x_dir):
        if x_dir == 'left':
            for b in self.balls:
                b.xvel -= 100
        elif x_dir == 'right':
            for b in self.balls:
                b.xvel += 100

    def check_action(self):
        for b in self.balls:
            if len(b.action) > 0:
                return False
        return True

class Ball(Drawable):
    def __init__(self, x, y, wid, win):
        super().__init__(x, y, wid)
        self.cir = gr.Circle(gr.Point(x, y), wid / 2)
        self.cir.setFill('blue')
        self.cir.draw(win)
        self.action = []

    def update(self, ene, sce, ind):
        yvel1 = self.yvel0 - 200 * time
        if self.ypos + time * (self.yvel0 + yvel1) / 2.0 <= self.rest_y:
            move_y = self.rest_y - self.ypos
        else:
            move_y = time * (self.yvel0 + yvel1) / 2.0
        self.ypos += move_y
        self.yvel0 = yvel1
        self.xpos += time * self.xvel
        self.cir.move(0, move_y)
        if self.xpos < 500:
            self.cir.move(time * self.xvel, 0)
        elif ind == 0:                                 # only move enemy/scenery once, not 3x (once for each ball in snowman)
            for e in ene:
                e.sq.move(-time * self.xvel, 0)        # visually move enemies, not hero
            for s in sce:
                s.trunk.move(-time * self.xvel, 0)     # visually move scenery, not hero
                s.branch1.move(-time * self.xvel, 0)
                s.branch2.move(-time * self.xvel, 0)
                s.branch3.move(-time * self.xvel, 0)

    def crouch(self, dy):
        dy *= self.ypos                                # reduce ypos ('height') for each ball by %
        self.ypos -= dy
        self.cir.move(0, -dy)

    def set_pound(self, ct):
        self.action.append(('pound', ct))              # set a pound for a future l_ct

    def pound(self):
        self.yvel0 = -400                              # execute pound

    def set_dbl_jump(self, ct):
        self.yvel0 = max(self.yvel0, 40)
        for i in range(3):
            self.action.append(('dbl_jump', ct + i))   # set a jump for a future l_ct

    def dbl_jump(self):
        self.ypos += 30
        self.cir.move(0, 30)

    def jump(self):
        self.yvel0 = 300                               # jump, both regular and mid-air


class Enemy(Drawable):
    def __init__(self, x, y, wid, xvel, win):
        super().__init__(x, y, wid, xvel)
        self.sq = gr.Rectangle(gr.Point(x - wid/2, wid), gr.Point(x + wid/2, 0))
        self.sq.setFill('red')
        self.sq.draw(win)

    def update(self, balls):
        if random.randrange(10) == 0 and self.ypos == self.rest_y:
            self.yvel0 = 250
        if balls[0].xpos > self.xpos:
            self.xvel = abs(self.xvel)
        else:
            self.xvel = -abs(self.xvel)
        yvel1 = self.yvel0 - 200 * time
        if self.ypos + time * (self.yvel0 + yvel1) / 2.0 <= self.rest_y:
            move_y = self.rest_y - self.ypos
            self.yvel0 = 0
        else:
            move_y = time * (self.yvel0 + yvel1) / 2.0
            self.yvel0 = yvel1
        self.ypos += move_y
        self.xpos += time * self.xvel
        self.sq.move(time * self.xvel, move_y)


class Shooter(Drawable):
    def __init__(self, x, y, wid, win, bull):
        super().__init__(x, y, wid)
        self.tri = gr.Polygon(gr.Point(self.xpos - self.wid/2, self.ypos - self.wid/2),
                              gr.Point(self.xpos + self.wid/2, self.ypos + self.wid/2),
                              gr.Point(self.xpos, self.ypos - self.wid/2))
        self.tri.draw(win)
        self.bull = bull


class Bullet(Drawable):
    def __init__(self, x, y, wid, win):
        super().__init__(x, y, wid)
        self.ln = gr.Line(gr.Point(self.xpos - self.wid/2, self.ypos - self.wid/2),
                          gr.Point(self.xpos + self.wid/2, self.ypos + self.wid/2))
        self.ln.draw(win)


class Sword(Drawable):
    def __init__(self, x, y, wid, win):
        super().__init__(x, y, wid)
        self.ln = gr.Line(gr.Point(self.xpos - self.wid / 2, self.ypos - self.wid / 2),
                          gr.Point(self.xpos + self.wid / 2, self.ypos + self.wid / 2))
        self.ln.draw(win)


class Prize(Drawable):
    def __init__(self, x, y, wid, win):
        super().__init__(x, y, wid, random.randrange(-1, 2))
        self.cir = gr.Circle(gr.Point(x, y), 20)
        self.cir.setFill('green')
        self.cir.draw(win)


class Tree:
    def __init__(self, x, win):
        self.x = x
        self.trunk = gr.Rectangle(gr.Point(x - 5, 30), gr.Point(x + 5, 0))
        self.trunk.setFill('brown')
        self.trunk.draw(win)
        self.branch1 = gr.Polygon(gr.Point(x - 30, 30), gr.Point(x + 30, 30), gr.Point(x, 70))
        self.branch1.setFill('green')
        self.branch1.draw(win)
        self.branch2 = gr.Polygon(gr.Point(x - 25, 50), gr.Point(x + 25, 50), gr.Point(x, 85))
        self.branch2.setFill('green')
        self.branch2.draw(win)
        self.branch3 = gr.Polygon(gr.Point(x - 20, 70), gr.Point(x + 20, 70), gr.Point(x, 100))
        self.branch3.setFill('green')
        self.branch3.draw(win)


def main():
    w = 1000
    h = 400
    l_ct = 0
    prize = []
    win = gr.GraphWin('ANGRY SNOWMAN', w, h)
    win.setCoords(0, 0, w, h)
    sce = []
    for i in range(10):
        sce.append(Tree(500 + i * random.randrange(100, 1000), win))
    tim = Hero(win)
    ene = [Enemy(800, 20, 40, -50, win), Enemy(1000, 20, 40, -70, win), Enemy(1200, 20, 40, -50, win)]
    while True:
        l_ct += 1
        sleeper.sleep(time)
        if tim.state == 'crouched':              # if crouched, grab items within reach
            for p in prize:
                p.check(tim)
        ck = win.checkKey().lower()
        if ck == 'down' or ck == 'up':
            tim.update(ck, l_ct, ene, sce)
        elif ck == 'left' or ck == 'right':
            tim.change_dir(ck)
        else:
            tim.update('', l_ct, ene, sce)

        for e in ene:
            e.update(tim.balls)


score = main()


