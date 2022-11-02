import numpy as np
from PIL import Image, ImageDraw

outputFileName = 'C:/Users/79371/Desktop/python apps/psycho/1.png'
w = 500
h = 500
mode = 'RGBA'
bgColor = (0, 0, 0, 0)
circleColor = (0, 0, 0, 255)

imOut = Image.new(mode, (w, h), bgColor)
draw = ImageDraw.Draw(imOut)

for i in range(w):
    for j in range(h):
        if (i-w/2)**2 + (j-h/2)**2 <= (w/2)**2:
            if not (j < h/2 and np.abs((i-w/2)/(j-h/2)) < 1): 
                draw.point((i, j), circleColor)

imOut.save(outputFileName)