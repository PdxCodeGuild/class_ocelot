
import colorsys
from PIL import Image
import random

img = Image.open('Lenna.png')
w, h = img.size
pixels = img.load()


for i in range(0, w, 2):
    for j in range(h):
        r, g, b = pixels[i // 2, j]
        if r > g and r > b:
            pixels[i // 2, j] = (max(r - 50, 0), min(g + 100, 255), min(b + 100, 255))
        if g > r and g > b:
            pixels[i // 2, j] = (max(r + 100, 0), min(g - 50, 255), min(b + 100, 255))
        else:
            pixels[i // 2, j] = (max(r + 100, 0), min(g + 100, 255), min(b - 50, 255))

img.show()
