import PIL, colorsys, random, time, math

from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(int(height/255)):
        r, g, b = pixels[i, j]

        # your code here
        # time.sleep(1)
        # r = height/2
        # r -= random.randrange(255)
        # r = r + 255
        r = r
        if r > 255:
            r = 255
        if r < 0:
            r = 0

        pixels[i, j] = (r, g, b)

img.show()

# print(width, height)

