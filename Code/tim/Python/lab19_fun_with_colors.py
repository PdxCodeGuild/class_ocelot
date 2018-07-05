
import colorsys
# import PIL
from PIL import Image

# print(PIL.PILLOW_VERSION)

img = Image.open('game_enemy_robot_wasp_shot.png')
w, h = img.size
pixels = img.load()

for i in range(w):
    for j in range(h):
        r, g, b, a = pixels[i, j]
        if not (r == g == b):
            if abs(r - g) < 100:
                pixels[i, j] = (r, int(g*.7), int(b*1.1), 255)

img = img.convert("RGB")
img.save('orange_wasp.png')
