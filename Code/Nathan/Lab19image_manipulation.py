
from PIL import Image, ImageDraw, ImageFont

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

draw = ImageDraw.Draw(img)
color = (256, 128, 228)
draw.line((0, 0, width, height), fill=color)
draw.line((100, width, height,0), fill=color)


# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

        # your code here

     #   pixels[i, j] = (r, g, b)

img.show()