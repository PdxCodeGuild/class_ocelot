import random
import chalk


def print_grid(g, h, w):  # Borrowed from Conway labXX
    p_grid = ''
    for i in range(h):
        for j in range(w):
            if g[j][i]:
                try:
                    if not g[j-1][i] and not g[j+1][i]:
                        p_grid += chalk.blue ('■')
                    elif g[j-1][i] and g[j+1][i] and not g[j][i-1]:
                        p_grid += chalk.red('■')
                    else:
                        p_grid += '■'
                except:
                    p_grid += '■'
                    continue
            else:
                p_grid += '□'
        p_grid += '\n'
    print(p_grid)


h = 20
w = 100
g = []
t = 10
force_dir = False
force_dir_ct = 0
d = 0
for j in range(w):
    g.append([])
    if t >= h - 2:
        d = -1
        force_dir = True
    elif t <= 1:
        d = 1
        force_dir = True
    elif j % 2 == 0 and not force_dir:
        d = 1 if random.randrange(2) == 0 else -1
    t += d
    for i in range(t):
        g[j].append(False)
    for i in range(t, h):
        g[j].append(True)
    if force_dir:
        if force_dir_ct > 0:
            force_dir_ct = 0
            force_dir = False
        else:
            force_dir_ct += 1
print_grid(g, h, w)
