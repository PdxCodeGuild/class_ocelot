import graphics as gr
import math
import time as sleeper
import random


class Balls:

    def __init__(self, win, ball, r):
        self.ball = ball
        self.cir = gr.Circle(gr.Point(ball.getX(), ball.getY()), r)
        if r > 3:
            self.cir.setFill('Blue')

        else:
            self.cir.setFill('Yellow')
        self.cir.draw(win)

    def update(self, o_ct, win):
        p = self.cir.getCenter()
        x = p.getX()
        y = p.getY()
        self.cir.move(self.ball.getX() - x, self.ball.getY() - y)
        if o_ct > 0:
            if o_ct % 2 == 0:
                self.cir.undraw()
            else:
                self.cir.draw(win)

    def delete(self):
        self.cir.undraw()


class Bouncy:

    def __init__(self, ang, vel, hei):
        self.xpos = 0.0
        self.ypos = hei
        theta = math.radians(ang)
        self.xvel = vel * math.cos(theta)
        self.yvel0 = vel * math.sin(theta)

    def update(self, time, w, ang, vel, a_zone, b_dir, b_pos):
        if b_dir != '' and b_pos == 0 and self.ypos + time * (self.yvel0 * 2 - 70 * time) / 2.0 <= 0:
            set_action_zone(self.xpos + time * self.xvel, 0, b_dir, a_zone)
            b_dir = ''
        for a in a_zone:
            if a[0] + .5 > self.xpos > a[0] - .5 and a[1] + .5 > self.ypos > a[1] - .5 and b_pos == a[3]:
                if a[2] == 'up':
                    self.flutter(vel)
                    a[3] += 1
                elif a[2] == 'down':
                    self.plunge()
                    a[3] += 1
        yvel1 = self.yvel0 - 140 * time
        self.ypos += time * (self.yvel0 + yvel1) / 2.0
        self.yvel0 = yvel1
        self.xpos += time * self.xvel
        if self.xpos > w:
            self.reset_left()
        elif self.xpos <= 0:
            self.reset_right(w)
        if self.ypos < 0:
            self.bounce(ang, vel)
        for a in a_zone:
            if a[0] + .5 > self.xpos > a[0] - .5 and a[1] + .5 > self.ypos > a[1] - .5 and b_pos == a[3]:
                if a[2] == 'left':
                    self.xvel = -abs(self.xvel)
                    a[3] += 1
                elif a[2] == 'right':
                    self.xvel = abs(self.xvel)
                    a[3] += 1
        return b_dir

    def plunge(self):
        self.yvel0 = -400

    def bounce(self, ang, vel):
        theta = math.radians(ang)
        max_vel = vel * math.sin(theta)
        self.yvel0 = min(abs(self.yvel0), max_vel)
        self.ypos = 0.0
        self.yvel0 *= .95

    def flutter(self, vel):
        self.yvel0 = vel * .32

    def getY(self):  # didn't work with name "get_y"?
        return self.ypos

    def getX(self):  # didn't work with name "get_x"?
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
        yvel1 = self.yvel0 + 140 * time
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
        self.ov = gr.Oval(gr.Point(r - tar_wid, h), gr.Point(r, h + 5))
        self.ov.setFill('green')
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


class Monster:

    def __init__(self, win, r, mon_wid, mon_max_vel, mon_acc):
        self.xpos = r - mon_wid / 2
        self.ypos = mon_wid / 2
        self.yvel0 = 0
        self.xvel0 = 0
        self.sq = gr.Rectangle(gr.Point(r - mon_wid, 0), gr.Point(r, mon_wid))
        self.sq.setFill('Red')
        self.sq.draw(win)
        self.max_vel = mon_max_vel
        self.acc = mon_acc

    def move(self, time, x, j_speed, mon_wid):
        if j_speed > 0:
            yvel1 = self.yvel0 + j_speed
        else:
            yvel1 = self.yvel0 - 180 * time
        move_y = (self.yvel0 + yvel1) / 2
        if self.ypos + move_y <= mon_wid / 2:
            move_y = mon_wid / 2 - self.ypos
            self.yvel0 = 0
        else:
            self.yvel0 = yvel1
        self.ypos += move_y
        if self.xpos >= x:
            xvel1 = min(self.xvel0 - self.acc, self.max_vel)
            self.sq.move(time * (self.xvel0 + xvel1) / 2, move_y)
            self.xpos += time * (self.xvel0 + xvel1) / 2
            self.xvel0 = xvel1
        else:
            xvel1 = max(self.xvel0 + self.acc, -self.max_vel)
            self.sq.move(time * (self.xvel0 + xvel1) / 2, move_y)
            self.xpos += time * (self.xvel0 + xvel1) / 2
            self.xvel0 = xvel1

    def check_hit(self, yvel, bx, by, mon_wid):
        if self.xpos - mon_wid / 2 <= bx <= self.xpos + mon_wid / 2 and self.ypos - mon_wid / 2 <= by <= self.ypos + mon_wid / 2:
            if yvel < -300 and self.yvel0 >= 0:
                return 'pop'
            else:
                return 'ouch'

    def new_target(self, r):
        self.sq.move(r, 0)
        self.xpos += r
        self.xvel0 = 0.0

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def delete(self):
        self.sq.undraw()


class Minion:

    def __init__(self, win, x, min_wid, min_jump):
        self.xpos = x + 100
        self.ypos = min_wid / 2
        self.yvel0 = 0
        self.xvel = 0
        self.tri = gr.Polygon(gr.Point(x + 100 - min_wid / 2, 0), gr.Point(x + 100 + min_wid / 2, 0), gr.Point(x + 100, min_wid))
        self.tri.setFill('Red')
        self.tri.draw(win)
        self.jump = min_jump * 3
        self.wid = min_wid

    def update(self, time):
        yvel1 = 0
        if self.ypos > self.wid / 2 or self.yvel0 > 0:
            yvel1 = self.yvel0 - 180 * time
        move_y = time * (self.yvel0 + yvel1) / 2
        if self.ypos + move_y <= self.wid / 2:
            move_y = self.wid / 2 - self.ypos
            self.yvel0 = 0
            self.xvel = 0
        else:
            self.yvel0 = yvel1
        self.xpos += time * self.xvel
        self.ypos += move_y
        self.tri.move(time * self.xvel, move_y)

    def shrink(self, t, min_wid, win):
        self.tri.undraw()
        self.tri = gr.Polygon(gr.Point(self.getX() - self.wid / 2, 0), gr.Point(self.getX() + self.wid / 2, 0),
            gr.Point(self.getX(), min_wid))
        self.tri.setFill('Red')
        self.tri.draw(win)

    def hop(self, x, min_wid, win):
        self.tri.undraw()
        self.tri = gr.Polygon(gr.Point(self.getX() - min_wid / 2, 0), gr.Point(self.getX() + min_wid / 2, 0),
            gr.Point(self.getX(), min_wid))
        self.tri.setFill('Red')
        self.tri.draw(win)
        theta = math.radians(45)
        self.xvel = self.jump * math.cos(theta) * (1 if self.xpos < x else -1)
        self.yvel0 = self.jump * math.sin(theta)

    def check_hit(self, yvel, bx, by):
        eps = self.wid / 2 * 1.1
        if self.getX() - eps <= bx <= self.getX() + eps and self.getY() - eps <= by <= self.getY() + eps:
            if yvel < -300:
                return 'pop'
            else:
                return 'ouch'

    def new_target(self, r):
        self.tri.move(r, 0)
        self.xpos += r
        self.xvel0 = 0.0

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def delete(self):
        self.tri.undraw()


class Silo:

    def __init__(self, win, x, min_wid, min_jump):
        self.xpos = x
        self.tri = gr.Polygon(gr.Point(x - min_wid / 2, 0), gr.Point(x + min_wid / 2, 0), gr.Point(x, min_wid * 2))
        self.tri.setFill('Red')
        self.tri.draw(win)
        self.jump = min_jump * 3
        self.wid = min_wid


# class Missle:



def set_action_zone(x, y, ck, a_zone):
    a_zone.append([x, y, ck, 0])


def get_inputs():
    a = int(input('What difficulty level?\n > '))
    if a == 1:
        settings = [100, 0, 0, 60, 0, 0, 0, 100, 30] # t_size, t_vel, t_acc, m_size, m_vel, m_acc, j_speed, j_freq, min_wid
    elif a == 2:
        settings = [90, 10, 1, 60, 6, .8, 40, 60, 30] # t_size, t_vel, t_acc, m_size, m_vel, m_acc, j_speed, j_freq, min_wid
    elif a == 3:
        settings = [80, 16, 1.5, 60, 16, 1, 50, 50, 30] # t_size, t_vel, t_acc, m_size, m_vel, m_acc, j_speed, j_freq, min_wid
    elif a == 4:
        settings = [70, 24, 1.8, 60, 24, 1.2, 64, 40, 30] # t_size, t_vel, t_acc, m_size, m_vel, m_acc, j_speed, j_freq, min_wid
    else:
        settings = [50, 34, 2, 60, 30, 1.5, 80, 30, 30] # t_size, t_vel, t_acc, m_size, m_vel, m_acc, j_speed, j_freq, min_wid
    return settings[0], settings[1], settings[2], settings[3], settings[4], settings[5], settings[6], settings[7], settings[8]


def get_lit():
    w = 1500
    h = 600
    l_ct = 0
    f_ct = 0
    o_ct = 0
    score = 0
    turn = 0
    ang = 55
    vel = 400
    freq = 2
    hei = 80
    time = .05
    b_balls = []
    f_balls = []
    a_zone = []
    b_dir = ''
    hit = False
    return w, h, l_ct, f_ct, o_ct, score, turn, ang, vel, freq, hei, time, b_balls, f_balls, a_zone, b_dir, hit


def random_dir():
    return 1 if random.randrange(2) == 1 else -1


def main():

    w, h, l_ct, f_ct, o_ct, score, turn, ang, vel, freq, hei, time, b_balls, f_balls, a_zone, b_dir, hit = get_lit()
    tar_wid, tar_max_vel, tar_acc, mon_wid, mon_max_vel, mon_acc, j_speed, j_freq, min_wid = get_inputs()
    win = gr.GraphWin('BUBBLE SNAKE BASKETBALL', w, h)
    win.setCoords(0, 0, w, h)

    tx = random.randrange(w // 2, w) - 10
    mx = random.randrange(w // 2, w) - 10
    tar = Target(win, tx, h - 5, tar_wid, tar_max_vel, tar_acc)
    mon = Monster(win, mx, mon_wid, mon_max_vel, mon_acc)
    mini = Minion(win, mx, min_wid, j_speed)

    while True:

        sleeper.sleep(time)
        l_ct += 1
        if l_ct % freq == 1 and len(b_balls) + f_ct < 10:
            b = Bouncy(ang, vel, hei)
            t = Balls(win, b, 3)
            b_balls.append([b, t])
        if l_ct > 20:
            if l_ct % (freq * 40) == 0:
                mini.hop(mon.getX(), min_wid, win)
                l_ct = 0
            elif l_ct % (freq * 5) == 0 and mini.getY() <= min_wid / 2:
                mini.shrink((l_ct - 20) // (freq * 5), min_wid, win)

        ck = win.checkKey().lower()
        if ck == 'space':
            b = Floater(b_balls[0][0].getX(), b_balls[0][0].getY(), b_balls[0][0].xvel, b_balls[0][0].yvel0)
            t = Balls(win, b, 5)
            f_balls.append([b, t])
            b_balls[0][1].delete()
            b_balls.remove(b_balls[0])
            f_ct += 1
        elif ck != '' and len(b_balls) > 0:
            if ck == 'left' or ck == 'right':
                b_dir = ck
            else:
                set_action_zone(b_balls[0][0].getX(), b_balls[0][0].getY(), ck, a_zone)

        if o_ct > 0:
            if o_ct > 30:
                hit = False
                o_ct = 0
            else:
                o_ct += 1

        for b in b_balls:
            if o_ct == 0:
                mon_ck = mon.check_hit(b[0].yvel0, b[0].getX(), b[0].getY(), mon_wid)
                if mon_ck == 'pop':
                    puff = -random.randrange(10, 50)
                    for i in range(3):
                        nb = Floater(mon.getX(), mon_wid / 2, puff, 0)
                        t = Balls(win, nb, 5)
                        f_balls.append([nb, t])
                        puff += random.randrange(10, 50)
                    mon.new_target(random.randrange(.2 * w, .3 * w) * random_dir())
                elif mon_ck == 'ouch':
                    hit = True
                min_ck = mini.check_hit(b[0].yvel0, b[0].getX(), b[0].getY())
                if min_ck == 'pop':
                    puff = -random.randrange(20, 50)
                    for i in range(3):
                        nb = Floater(mini.getX(), min_wid / 2, puff, 0)
                        t = Balls(win, nb, 5)
                        f_balls.append([nb, t])
                        puff += random.randrange(20, 50)
                    mini.new_target(random.randrange(.2 * w, .3 * w) * random_dir())
                elif min_ck == 'ouch':
                    hit = True
            b_dir = b[0].update(time, w, ang, vel, a_zone, b_dir, b_balls.index(b))
            b[1].update(o_ct, win)

        if len(b_balls) > 0:
            x = b_balls[0][0].getX()
        else:
            x = w // 2
        mon.move(time, x, (random.randrange(j_freq) == 0 and mon.getY() <= mon_wid / 2) * j_speed, mon_wid)
        mini.update(time)

        if hit and o_ct == 0:
            nb = Floater(b_balls[0][0].getX(), b_balls[0][0].getY(), b_balls[0][0].xvel, b_balls[0][0].yvel0)
            t = Balls(win, nb, 5)
            f_balls.append([nb, t])
            b_balls[0][1].delete()
            b_balls.remove(b_balls[0])
            o_ct = 1
            f_ct += 1
            for a in a_zone:
                a[3] -= 1

        for a in a_zone:
            if a[3] >= len(b_balls):
                a_zone.remove(a)

        t = tar.move(time, x, w)
        if t == 'over':
            tar.new_target(-random.randrange(w // 3, 2 * w // 3))
        elif t == 'under':
            tar.new_target(random.randrange(w // 3, 2 * w // 3))

        for f in f_balls:
            f[0].update(time, w)
            f[1].update(0, win)
            if f[0].getY() > h - 5:
                if tar.check_floater(f[0].getX(), tar_wid):
                    score += 1
                    tar.new_target(random.randrange(0, w // 2))
                f[1].delete()
                f_balls.remove(f)
                if f_ct == 10 and len(f_balls) == 0:
                    return score


print(f'You got a {main()}')
