import graphics as gr
import math
import time as sleeper
import random

class Balls:

    def __init__(self, win, ball, r):
        self.ball = ball
        self.cir = gr.Circle(gr.Point(ball.getX(), ball.getY()), r)
        if r > 3:
            self.cir.setFill('blue')

        else:
            self.cir.setFill('yellow')
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
                try:
                    self.cir.draw(win)
                except:
                    pass

    def delete(self):
        self.cir.undraw()


class Bouncy:

    def __init__(self, ang, vel, hei, x_pos, y_pos, x_vel, y_vel):
        if x_pos > 0:
            self.xpos = x_pos
            self.ypos = y_pos
            self.xvel = x_vel
            self.yvel0 = y_vel
        else:
            self.xpos = 0
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
        self.sq.setFill('red')
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
        in_x = self.xpos - mon_wid / 2 * 1.05 <= bx <= self.xpos + mon_wid / 2 * 1.05
        in_y = self.ypos - mon_wid / 2 * 1.05 <= by <= self.ypos + mon_wid / 2 * 1.05
        if in_x and in_y:
            if yvel <= -350 and self.yvel0 >= 0:
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
        self.tri = gr.Polygon(gr.Point(x + 100 - min_wid / 2, 0), gr.Point(x + 100 + min_wid / 2, 0),
                              gr.Point(x + 100, min_wid))
        self.tri.setFill('red')
        self.tri.draw(win)
        self.jump = min_jump * 3
        self.wid = min_wid

    def update(self, time, min_wid):
        yvel1 = 0
        if self.ypos > min_wid / 2 or self.yvel0 > 0:
            yvel1 = self.yvel0 - 180 * time
        move_y = time * (self.yvel0 + yvel1) / 2
        if self.ypos + move_y <= min_wid / 2 and self.yvel0 < 0:
            move_y = min_wid / 2 - self.ypos
            self.yvel0 = 0
            self.xvel = 0
        else:
            self.yvel0 = yvel1
        self.xpos += time * self.xvel
        self.ypos += move_y
        self.tri.move(time * self.xvel, move_y)

    def shrink(self, t, min_wid, win):
        if t > 1:
            off_x = min_wid * t / 2
            self.tri.undraw()
            self.tri = gr.Polygon(gr.Point(self.getX() - off_x, 0), gr.Point(self.getX() + off_x, 0),
                                  gr.Point(self.getX(), min_wid / t))
            self.tri.setFill('purple')
            self.tri.draw(win)
            self.wid = off_x * 2
            self.ypos = min_wid / t / 2
            # print(self.wid, self.ypos)

    def hop(self, x, min_wid, win):
        self.tri.undraw()
        self.tri = gr.Polygon(gr.Point(self.getX() - min_wid / 2, 0), gr.Point(self.getX() + min_wid / 2, 0),
                              gr.Point(self.getX(), min_wid))
        self.tri.setFill('red')
        self.tri.draw(win)
        theta = math.radians(45)
        self.xvel = self.jump * math.cos(theta) * (1 if self.xpos < x else -1) * (1 + random.randint(1, 151) / 100)
        self.yvel0 = self.jump * math.sin(theta)
        self.wid = min_wid
        self.ypos = min_wid / 2

    def check_hit(self, bv, bx, by, min_wid):
        eps = self.wid / 2 * 1.02
        if self.getX() - eps <= bx <= self.getX() + eps and self.getY() - eps * 2 <= by <= self.getY() * 2.02:
            if bv <= -350 or bv == 0:
                if self.wid > min_wid:
                    return 'bonus'
                else:
                    return 'pop'
            else:
                return 'ouch'

    def new_target(self, r, min_wid, win):
        new_x = self.xpos + r
        self.tri.undraw()
        self.tri = gr.Polygon(gr.Point(new_x - min_wid / 2, 0), gr.Point(new_x + min_wid / 2, 0),
                              gr.Point(new_x, min_wid))
        self.tri.setFill('red')
        self.tri.draw(win)
        self.xpos = new_x
        self.ypos = min_wid / 2
        self.wid = min_wid
        self.xvel0 = 0

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def delete(self):
        self.tri.undraw()


class Silo:

    def __init__(self, win, x, min_wid, s_shot, s_life, s_vel):
        self.xpos = x
        self.tri = gr.Polygon(gr.Point(x - min_wid / 2, 0), gr.Point(x + min_wid / 2, 0), gr.Point(x, min_wid))
        self.tri.setFill('grey')
        self.tri.draw(win)
        self.shots = s_shot
        self.life = s_life
        self.wid = min_wid
        self.s_vel = s_vel

    def fire(self, win, bx, missiles, time):
        if self.xpos < bx:
            s_dir = -1
        else:
            s_dir = 1
        s_ang = 90
        add_close = int(abs(bx - self.xpos) // 100)
        for a in range(add_close):
            s_ang += random.randint(5, 7) * s_dir
        for i in range(self.shots):
            missiles.append(Missile(win, self.xpos, self.wid / 2, s_ang + i * 4, self.s_vel, time))
        self.life -= 1
        self.tri.setFill('black')

    def check_hit(self, bx, by):
        x_eps = self.wid / 2 * 1.05
        if self.getX() - x_eps <= bx <= self.getX() + x_eps and 0 <= by <= x_eps:
            return 'pop'

    def get_life(self):
        return self.life

    def getX(self):
        return self.xpos

    def die(self):
        self.tri.undraw()


class Missile:

    def __init__(self, win, x, y, ang, vel, time):
        self.xpos = x
        self.ypos = y
        theta = math.radians(ang)
        self.xvel = vel * math.cos(theta)
        self.yvel = vel * math.sin(theta)
        x2 = x + self.xvel * time
        y2 = y + self.yvel * time
        self.line = gr.Line(gr.Point(x, y), gr.Point(x2, y2))
        self.line.draw(win)

    def update(self, time, w, h):
        self.ypos += time * self.yvel
        self.xpos += time * self.xvel
        self.line.move(time * self.xvel, time * self.yvel)
        if self.xpos > w or self.xpos < 0 or self.ypos > h:
            self.line.undraw()
            return 'off'

    def check_hit(self, bx, by, time):
        x_eps = abs(time * self.xvel / 2) + 2
        y_eps = time * self.yvel / 2 + 2
        if self.getX() - x_eps <= bx <= self.getX() + x_eps and self.getY() - y_eps <= by <= self.getY() + y_eps:
            return 'ouch'

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos


class Bonus:

    def __init__(self, win, x):
        self.xpos = x
        self.ypos = 1
        theta = math.radians(random.randrange(30, 71))
        self.xvel = 140 * math.cos(theta) * random_dir()
        self.yvel0 = 140 * math.sin(theta)
        self.cir = gr.Circle(gr.Point(x, 2.5), 5)
        self.cir.setFill('yellow')
        self.cir.draw(win)
        self.life = 200

    def update(self, win, time):
        yvel1 = 0
        if self.ypos > 0:
            yvel1 = self.yvel0 - 180 * time
        move_y = time * (self.yvel0 + yvel1) / 2
        if self.ypos + move_y <= 2.5:
            move_y = 2.5 - self.ypos
            self.yvel0 = 0
            self.xvel = 0
        else:
            self.yvel0 = yvel1
        self.xpos += time * self.xvel
        self.ypos += move_y
        self.cir.move(time * self.xvel, move_y)
        self.life -= 1
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
        elif 0 < self.life < 10:
            if self.life % 2 == 1:
                self.cir.undraw()
            else:
                self.cir.draw(win)
        elif self.life == 0:
            self.cir.undraw()
        return self.life

    def kill(self):
        self.cir.undraw()

    def check_hit(self, bx, by):
        if self.life < 175 and self.getX() - 10 <= bx <= self.getX() + 10 and  by <= 10:
            return 'pick'

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos


def set_action_zone(x, y, ck, a_zone):
    a_zone.append([x, y, ck, 0])


def get_inputs():
    a = 4 # int(input('What difficulty level?\n > '))
    # SETTINGS ORDER
    # t_size, t_vel, t_acc, m_size, m_vel, m_acc, j_speed, j_freq, min_wid, s_shot, s_life, s_vel
    if a == 1:
        sets = [100, 0, 0, 60, 0, 0, 0, 50, 30, 1, 1, 100]
    elif a == 2:
        sets = [90, 16, 1, 60, 6, .8, 40, 50, 30, 2, 2, 150]
    elif a == 3:
        sets = [80, 22, 1.5, 60, 16, 1, 50, 40, 30, 2, 3, 200]
    elif a == 4:
        sets = [70, 30, 1.8, 60, 24, 1.2, 60, 30, 30, 3, 3, 250]
    else:
        sets = [50, 40, 2, 60, 30, 1.5, 80, 20, 30, 3, 4, 300]
    return tuple(sets)


def get_lit():
    w = 1500
    h = 600
    l_ct = 0
    f_ct = 0
    o_ct = 0
    b_ct = 0
    score = 0
    turn = 0
    ang = 55
    vel = 400
    freq = 2
    hei = 80
    time = .05
    b_balls = []
    f_balls = []
    silos = []
    missiles = []
    a_zone = []
    bonuses = []
    pick_up = []
    b_dir = ''
    hit = False
    pick_bonus = False
    return w, h, l_ct, f_ct, o_ct, b_ct, score, turn, ang, vel, freq, hei, time, \
        b_balls, f_balls, silos, missiles, a_zone, bonuses, pick_up, b_dir, hit, pick_bonus


def random_dir():
    return 1 if random.randrange(2) == 1 else -1


def main():

    w, h, l_ct, f_ct, o_ct, b_ct, score, turn, ang, vel, freq, hei, time, \
        b_balls, f_balls, silos, missiles, a_zone, bonuses, pick_up, b_dir, hit, pick_bonus = get_lit()
    tar_wid, tar_max_vel, tar_acc, mon_wid, mon_max_vel, mon_acc, j_speed, j_freq, \
        min_wid, s_shot, s_life, s_vel = get_inputs()
    win = gr.GraphWin('BUBBLE SNAKE BASKETBALL', w, h)
    win.setCoords(0, 0, w, h)

    tx = random.randrange(w // 2, w) - 10
    mx = random.randrange(w // 2, w) - 10
    tar = Target(win, tx, h - 5, tar_wid, tar_max_vel, tar_acc)
    mon = Monster(win, mx, mon_wid, mon_max_vel, mon_acc)
    mini = Minion(win, mx, min_wid, j_speed)
    sb_header = gr.Text(gr.Point(.02 * w, .99 * h), 'SCORE')
    sb_header.draw(win)
    sb_score = gr.Text(gr.Point(.02 * w, .96 * h), 0)
    sb_score.draw(win)

    while True:

        sleeper.sleep(time)
        l_ct += 1
        if l_ct % freq == 1 and b_ct < 10:
            b = Bouncy(ang, vel, hei, 0, 0, 0, 0)
            t = Balls(win, b, 3)
            b_balls.append([b, t])
            b_ct += 1
        elif l_ct > j_freq and len(b_balls) > 0:
            if l_ct % (j_freq * 3) == 0:
                for s in silos:
                    s.fire(win, b_balls[0][0].getX(), missiles, time)
                ns = Silo(win, mini.getX(), min_wid, s_shot, s_life, s_vel)
                silos.append(ns)
                mini.hop(mon.getX(), min_wid, win)
                l_ct = 0
            elif l_ct == j_freq + 4:
                for s in silos:
                    if s.life == 0:
                        b = Floater(s.getX(), min_wid / 2, 0, 0)
                        t = Balls(win, b, 7)
                        f_balls.append([b, t])
                        s.die()
                        silos.remove(s)
            elif mini.getY() <= min_wid / 2:
                mini.shrink((l_ct - j_freq) / j_freq, min_wid, win)

        if len(pick_up) > 0:
            if pick_up[0] == 2:
                b = Bouncy(0, 0, 0, pick_up[1], pick_up[2], pick_up[3], pick_up[4])
                t = Balls(win, b, 3)
                b_balls.append([b, t])
                pick_up = []
            else:
                pick_up[0] += 1

        ck = win.checkKey().lower()
        if ck == 'space':
            b = Floater(b_balls[0][0].getX(), b_balls[0][0].getY(), b_balls[0][0].xvel, b_balls[0][0].yvel0)
            t = Balls(win, b, 7)
            f_balls.append([b, t])
            b_balls[0][1].delete()
            b_balls.remove(b_balls[0])
            f_ct += 1
            for a in a_zone:
                a[3] -= 1
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

        if len(b_balls) > 0:
            x = b_balls[0][0].getX()
        else:
            x = w // 2
        mon.move(time, x, (random.randrange(j_freq) == 0 and mon.getY() <= mon_wid / 2) * j_speed, mon_wid)
        mini.update(time, min_wid)
        for m in missiles:
            r = m.update(time, w, h)
            if r == 'off':
                missiles.remove(m)
        for b in bonuses:
            r = b.update(win, time)
            if r == 0:
                bonuses.remove(b)

        for b in b_balls:

            if o_ct == 0:
                mon_ck = mon.check_hit(b[0].yvel0, b[0].getX(), b[0].getY(), mon_wid)
                if mon_ck == 'pop':
                    puff = -random.randrange(10, 50)
                    for i in range(3):
                        nb = Floater(mon.getX(), mon_wid / 2, puff, 0)
                        t = Balls(win, nb, 7)
                        f_balls.append([nb, t])
                        puff += random.randrange(10, 50)
                    mon.new_target(random.randrange(.2 * w, .3 * w) * random_dir())
                elif mon_ck == 'ouch':
                    hit = True

                min_ck = mini.check_hit(b[0].yvel0, b[0].getX(), b[0].getY(), min_wid)
                if min_ck == 'bonus':
                    l_ct = 0
                    bonuses.append(Bonus(win, b[0].getX()))
                    mini.new_target(random.randrange(.2 * w, .3 * w) * random_dir(), min_wid, win)
                elif min_ck == 'pop':
                    l_ct = 0
                    puff = -random.randrange(20, 50)
                    for i in range(3):
                        nb = Floater(mini.getX(), min_wid / 2, puff, 0)
                        t = Balls(win, nb, 7)
                        f_balls.append([nb, t])
                        puff += random.randrange(20, 50)
                    mini.new_target(random.randrange(.2 * w, .3 * w) * random_dir(), min_wid, win)
                elif min_ck == 'ouch':
                    hit = True

                for m in missiles:
                    mis_ck = m.check_hit(b[0].getX(), b[0].getY(), time)
                    if mis_ck == 'ouch':
                        hit = True
                        break

            for bn in bonuses:
                bon_ck = bn.check_hit(b[0].getX(), b[0].getY())
                if bon_ck == 'pick':
                    pick_bonus = True
                    bn.kill()
                    bonuses.remove(bn)
                    break

            for s in silos:
                sil_ck = s.check_hit(b[0].getX(), b[0].getY())
                if sil_ck == 'pop':
                    nb = Floater(s.getX(), min_wid / 2, 0, 0)
                    t = Balls(win, nb, 7)
                    f_balls.append([nb, t])
                    s.die()
                    silos.remove(s)
                    break

            if pick_bonus and b is b_balls[-1]:
                pick_up = [1, b[0].getX(), b[0].getY(), b[0].xvel, b[0].yvel0]
                pick_bonus = False

            b_dir = b[0].update(time, w, ang, vel, a_zone, b_dir, b_balls.index(b))
            b[1].update(o_ct, win)

        if hit and o_ct == 0:
            nb = Floater(b_balls[0][0].getX(), b_balls[0][0].getY(), b_balls[0][0].xvel, b_balls[0][0].yvel0)
            t = Balls(win, nb, 7)
            f_balls.append([nb, t])
            b_balls[0][1].delete()
            b_balls.remove(b_balls[0])
            o_ct = 1
            f_ct += 1
            for a in a_zone:
                a[3] -= 1

        for a in a_zone:
            if a[3] >= len(b_balls) + (len(pick_up) > 0):
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
                    sb_score.setText(int(sb_score.getText()) + 1)
                    score += 1
                    tar.new_target(random.randrange(0, w // 2))
                f[1].delete()
                f_balls.remove(f)
                if len(b_balls) == 0 and len(f_balls) == 0:
                    return score


score = main()
if score < 20:
    print(f'YOU LOSE!!!!\nScore: {score}')
else:
    print('YOU WIN!!!!\nCongratulations')