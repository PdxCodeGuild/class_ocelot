import graphics as gr
import math
import time as sleeper
import random

time = .05
w = 1000
h = 400

enemies = []
prizes = []
scenery = []
snow_balls = []
weapons = []

win = gr.GraphWin('ANGRY SNOWMAN', w, h)


class Drawable:
    def __init__(self, x, y, wid, xvel=0, yvel0=0):
        self.xpos = x
        self.ypos = y
        self.rest_y = y
        self.xvel = xvel
        self.yvel0 = yvel0
        self.wid = wid


class Hero:
    def __init__(self):
        self.rest_y = 20
        self.hurt = 0
        self.state = ''
        self.balls = []
        next_y_spot = 0
        size = 40
        for i in range(3):
            size *= .8
            next_y_spot += size / 2  # Bottom half of current ball
            self.balls.append(Ball(200, next_y_spot, size))
            next_y_spot += size / 2  # Top half of current ball

    def update(self, action, l_ct):
        is_hurt = False
        if not self.check_action():
            if action == 'down':
                if self.balls[0].ypos > self.rest_y:  # check to see if you're mid-air
                    for i in range(len(self.balls)):
                        self.balls[i].set_pound(i * 3 + l_ct)
                else:  # otherwise crouch
                    self.state = 'crouched'
            elif action == 'up':
                if self.balls[0].ypos > self.rest_y:  # check to see if you're mid-air
                    for i in range(len(self.balls) - 1, -1, -1):
                        self.balls[i].set_dbl_jump(
                            (len(self.balls) - i) * 3 + l_ct)  # set a staggered jump, the disconnected ball effect
                else:
                    for b in self.balls:  # otherwise do a regular jump
                        b.jump()
        for i in range(len(self.balls)):  # loop through the balls
            for j in range(len(self.balls[i].action)):  # loop through the actions for each ball
                if j >= len(self.balls[i].action):  # fixes a bug as action list is depleted
                    continue
                if self.balls[i].action[j][
                    1] == l_ct:  # action list has tuple (action, l_ct), l_ct determines when to take action
                    if self.balls[i].action[j][0] == 'dbl_jump':
                        self.balls[i].dbl_jump()  # perform action
                        self.balls[i].action.remove(self.balls[i].action[j])  # remove action
                    elif self.balls[i].action[j][0] == 'pound':
                        self.balls[i].pound()  # perform action
                        self.balls[i].action.remove(self.balls[i].action[j])  # remove action
            first = (i == 0)  # "first" needed to know when to move non-balls
            is_hurt = self.balls[i].update(first, self.check_action(), self.hurt)  # result of update, including contact
            if self.state == 'crouched':
                for k in range(1, len(self.balls)):
                    self.balls[k].crouch(.2)
        if is_hurt:
            self.hurt = 40  # set hurt counter
        elif self.hurt > 0:
            self.hurt -= 1  # count down hurt

    def change_dir(self, x_dir):
        if x_dir == 'left':
            for b in self.balls:
                b.xvel -= 100  # momentum left +100
        elif x_dir == 'right':
            for b in self.balls:
                b.xvel += 100  # momentum right +100

    def check_action(self):
        for b in self.balls:  # see if you have a dbl_jump or pound, meaning you can hurt Enemy
            if len(b.action) > 0:
                return True
        return False


class Ball(Drawable):
    def __init__(self, x, y, wid):
        super().__init__(x, y, wid)
        self.cir = gr.Circle(gr.Point(x, y), wid / 2)
        self.cir.setFill('blue')
        self.cir.draw(win)
        self.action = []

    def update(self, first, action, hurt):
        is_hurt = False
        yvel1 = self.yvel0 - 200 * time
        if self.ypos + time * (self.yvel0 + yvel1) / 2.0 <= self.rest_y:
            move_y = self.rest_y - self.ypos
            self.yvel0 = 0
        else:
            move_y = time * (self.yvel0 + yvel1) / 2.0
        self.ypos += move_y
        self.xpos += time * self.xvel
        self.cir.move(0, move_y)
        if self.xpos < 500:
            self.cir.move(time * self.xvel, 0)
        elif first:  # visually move enemies, not hero
            for e in enemies:
                e.sq.move(-time * self.xvel, 0)
            for s in scenery:
                s.trunk.move(-time * self.xvel, 0)  # visually move scenery, not hero
                s.branch1.move(-time * self.xvel, 0)
                s.branch2.move(-time * self.xvel, 0)
                s.branch3.move(-time * self.xvel, 0)
            for s in snow_balls:  # visually move snow_balls, not hero
                s.cir.move(-time * self.xvel, 0)
            for p in prizes:  # visually move prizes, not hero
                p.tri.move(-time * self.xvel, 0)

        if hurt == 0:  # if you're not hurt, check contact with enemy
            for e in enemies:
                r = e.check_hit(self.xpos, self.ypos, self.wid, action or self.yvel0 <= -400,
                                int(self.cir.getCenter().getX()))
                if r == 'dead':  # process result of check_hit
                    enemies.remove(e)
                elif r == 'ouch':
                    is_hurt = True
        else:  # if you are hurt, blink on and off
            if hurt % 2 == 0:
                self.cir.undraw()
            else:
                self.cir.draw(win)
        self.yvel0 = yvel1
        return is_hurt  # result of update, to see if you need a hurt counter

    def crouch(self, dy):
        dy *= self.ypos  # reduce ypos ('height') for each ball by %
        self.ypos -= dy
        self.cir.move(0, -dy)

    def set_pound(self, ct):
        self.action.append(('pound', ct))  # set a pound for a future l_ct

    def pound(self):  # execute pound
        self.yvel0 = -400

    def set_dbl_jump(self, ct):  # set a jump to be performed at l_ct
        self.yvel0 = max(self.yvel0, 40)
        for i in range(3):  # dbl_jump is actually a series of ypos increases...
            self.action.append(('dbl_jump', ct + i))

    def dbl_jump(self):  # ... note that double jump does not effect velocity
        self.ypos += 30
        self.cir.move(0, 30)

    def jump(self):
        self.yvel0 = 300  # jump, both regular and mid-air


class Enemy(Drawable):
    def __init__(self, x, y, wid, xvel, draw_x=0):
        super().__init__(x, y, wid, xvel)
        self.life = 3
        self.hurt_ct = 0
        if draw_x > 0:
            self.sq = gr.Rectangle(gr.Point(draw_x - wid / 2, wid), gr.Point(draw_x + wid / 2, 0))
        else:
            self.sq = gr.Rectangle(gr.Point(x - wid / 2, wid), gr.Point(x + wid / 2, 0))
        self.sq.setFill('red')
        self.sq.draw(win)

    def update(self, balls):
        if self.ypos == self.rest_y:
            if random.randrange(10) == 0:  # randomly jump if on the ground
                self.yvel0 = 250
            if balls[0].xpos > self.xpos:  # change directions if on the ground and going the wrong way
                self.xvel = abs(self.xvel)
            else:
                self.xvel = -abs(self.xvel)
        yvel1 = self.yvel0 - 200 * time
        if self.ypos + time * (self.yvel0 + yvel1) / 2.0 <= self.rest_y:  # check to see if dy would put you underground
            move_y = self.rest_y - self.ypos
            self.yvel0 = 0
        else:
            move_y = time * (self.yvel0 + yvel1) / 2.0
            self.yvel0 = yvel1
        self.ypos += move_y
        self.xpos += time * self.xvel
        self.sq.move(time * self.xvel, move_y)

    def check_hit(self, x, y, wid, action, draw_x):
        in_x = x - wid / 2 < self.xpos + self.wid / 2 and self.xpos - self.wid / 2 < x + wid / 2
        in_y = y - wid / 2 < self.ypos + self.wid / 2 and self.ypos - self.wid < y + wid / 2
        if self.hurt_ct == 0:  # can't get hurt if already hurt
            if in_x and in_y:
                if not action:
                    return 'ouch'
                else:
                    return self.hurt(1, x, draw_x)
        else:  # blink if hurt
            self.hurt_ct -= 1
            if self.hurt_ct % 2 == 1:
                self.sq.undraw()
            else:
                self.sq.draw(win)

    def hurt(self, lives, x, draw_x):
        self.life -= lives
        if self.life == 2:  # change color as enemy loses life
            self.sq.setFill('purple')
        elif self.life == 1:
            self.sq.setFill('black')
        else:
            self.sq.undraw()
            self.pop(x, draw_x)
            return 'dead'
        self.hurt_ct = 40
        return 'hit'

    def pop(self, x, draw_x):
        prized = False
        for i in range(3):
            if not prized and random.randrange(10) < 1:  # random chance to get a prize
                xvel = random.randrange(50, 60) * random_dir()
                yvel = random.randrange(30, 40)
                prizes.append(Prize(self.xpos, self.ypos, 20, xvel, yvel, draw_x))
                prized = True
            else:  # otherwise you get snowballs (ie ammo)
                xvel = random.randrange(20, 60) * random_dir()
                yvel = random.randrange(30, 40)
                snow_balls.append(
                    SnowBall(self.xpos - max(x - w / 2, 0), self.ypos, 8, xvel, yvel, self.sq.getCenter().getX()))


class Prize(Drawable):
    def __init__(self, x, y, wid, xvel, yvel, draw_x):
        super().__init__(x, y, wid, xvel, yvel)
        self.tri = gr.Polygon(gr.Point(draw_x - wid / 2, y - wid / 2),
                              gr.Point(draw_x + wid / 2, y - wid / 2),
                              gr.Point(draw_x, y))
        self.tri.setFill('green')
        self.tri.draw(win)
        self.life = 200

    def update(self):
        yvel1 = self.yvel0 - 200 * time
        if self.ypos + time * (self.yvel0 + yvel1) / 2 <= self.wid / 2:
            move_y = self.wid / 2 - self.ypos
            self.yvel0 = 0
            self.xvel = 0
        else:
            move_y = time * (self.yvel0 + yvel1) / 2
            self.yvel0 = yvel1
        self.xpos += time * self.xvel
        self.ypos += move_y
        self.tri.move(time * self.xvel, move_y)
        if 80 <= self.life < 180:
            if self.life % 10 == 1:
                self.tri.undraw()
            elif self.life % 10 == 0:
                self.tri.draw(win)
        elif 20 <= self.life < 80:
            if self.life % 5 == 1:
                self.tri.undraw()
            elif self.life % 5 == 0:
                self.tri.draw(win)
        elif 0 < self.life < 20:
            if self.life % 2 == 1:
                self.tri.undraw()
            else:
                self.tri.draw(win)
        elif self.life == 0:
            self.tri.undraw()
            return 'dead'
        self.life -= 1

    def check_pick(self, ball0):
        if ball0 - 10 < self.xpos < ball0 + 10:
            self.tri.undraw()
            return True


class SnowBall(Drawable):
    def __init__(self, x, y, wid, xvel, yvel, draw_x):
        super().__init__(x, y, wid, xvel, yvel)
        self.cir = gr.Circle(gr.Point(draw_x, y), wid / 2)
        self.cir.setFill('blue')
        self.cir.draw(win)
        self.life = 200

    def update(self):
        yvel1 = self.yvel0 - 200 * time
        if self.ypos + time * (self.yvel0 + yvel1) / 2.0 <= self.wid / 2:
            move_y = self.wid / 2 - self.ypos
            self.yvel0 = 0
            self.xvel = 0
        else:
            move_y = time * (self.yvel0 + yvel1) / 2.0
            self.yvel0 = yvel1
        self.xpos += time * self.xvel
        self.ypos += move_y
        self.cir.move(time * self.xvel, move_y)
        if 80 <= self.life < 180:
            if self.life % 10 == 1:
                self.cir.undraw()
            elif self.life % 10 == 0:
                self.cir.draw(win)
        elif 20 <= self.life < 80:
            if self.life % 5 == 1:
                self.cir.undraw()
            elif self.life % 5 == 0:
                self.cir.draw(win)
        elif 0 < self.life < 20:
            if self.life % 2 == 1:
                self.cir.undraw()
            else:
                self.cir.draw(win)
        elif self.life == 0:
            self.cir.undraw()
            return 'dead'
        self.life -= 1


class SnowGun(Drawable):
    def __init__(self, x, y, wid, bull):
        super().__init__(x, y, wid)
        self.tri = gr.Polygon(gr.Point(self.xpos - self.wid / 2, self.ypos - self.wid / 2),
                              gr.Point(self.xpos + self.wid / 2, self.ypos + self.wid / 2),
                              gr.Point(self.xpos, self.ypos - self.wid / 2))
        self.tri.draw(win)
        self.bull = bull


class Bullet(Drawable):
    def __init__(self, x, y, wid):
        super().__init__(x, y, wid)
        self.ln = gr.Line(gr.Point(self.xpos - self.wid / 2, self.ypos - self.wid / 2),
                          gr.Point(self.xpos + self.wid / 2, self.ypos + self.wid / 2))
        self.ln.draw(win)


class Sword(Drawable):
    def __init__(self, x, y, wid):
        super().__init__(x, y, wid)
        self.ln = gr.Line(gr.Point(self.xpos - self.wid / 2, self.ypos - self.wid / 2),
                          gr.Point(self.xpos + self.wid / 2, self.ypos + self.wid / 2))
        self.ln.draw(win)


class Tree:
    def __init__(self, x):
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


def random_dir():
    return 1 if random.randrange(2) == 1 else -1


def main():
    tim = Hero()
    win.setCoords(0, 0, w, h)
    l_ct = 0
    for i in range(50):
        scenery.append(Tree(500 + i * random.randrange(100, 200)))
    enemies.append(Enemy(800, 20, 40, -random.randrange(100, 200)))
    enemies.append(Enemy(1000, 20, 40, -random.randrange(100, 200)))
    enemies.append(Enemy(1200, 20, 40, -random.randrange(100, 200)))
    while True:
        l_ct += 1
        sleeper.sleep(time)
        ck = win.checkKey().lower()
        if ck == 'left' or ck == 'right':
            tim.change_dir(ck)
        tim.update(ck, l_ct)
        if tim.state == 'crouched':  # if crouched, grab items within reach
            for p in prizes:
                if p.check_pick(tim.balls[0].xpos):
                    prizes.remove(p)
                    # weapons.append(SnowGun(tim.balls[0].xpos, ))
            tim.state = ''

        for e in enemies:
            e.update(tim.balls)
        for s in snow_balls:
            r = s.update()
            if r == 'dead':
                snow_balls.remove(s)
        for p in prizes:
            r = p.update()
            if r == 'dead':
                prizes.remove(p)

        if l_ct % 100 == 0 and len(enemies) < 6:
            enemies.append(Enemy(tim.balls[0].xpos + 500, 20, 40, -random.randrange(100, 200),
                                 tim.balls[0].cir.getCenter().getX() + 500))


score = main()


