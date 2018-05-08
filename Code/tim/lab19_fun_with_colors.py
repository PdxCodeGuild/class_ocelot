
import colorsys
from PIL import Image
import random

img = Image.open('Lenna.png')
w, h = img.size
pixels = img.load()

color_dict = {}
for r in range(256):
    for g in range(256):
        for b in range(256):
            rx = min(max(r + random.randrange(-50, 50), 0), 255)
            gx = min(max(g + random.randrange(-50, 50), 0), 255)
            bx = min(max(b + random.randrange(-50, 50), 0), 255)
            color_dict[(r, g, b)] = (rx, gx, bx)

for i in range(w):
    for j in range(h):
        r, g, b = pixels[i, j]
        pixels[i, j] = color_dict[(r, g, b)]

img.show()
