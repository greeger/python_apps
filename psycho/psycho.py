import numpy as np
from PIL import Image, ImageDraw

inputFileName = 'C:/Users/79371/Desktop/python apps/psycho/0.png'
outputFileName = 'C:/Users/79371/Desktop/python apps/psycho/rez.png'
w = 1000
h = 1000
mode = 'RGBA'
bgColor = (150, 150, 150, 255)
mainRadius = (int)(w/3)
circlesColor = (70, 70, 70, 255)
circleRadius = (int)(w/6)
seq = [2, 1, 4, 0, 3]
sizes = [1, 0.85, 0.7, 0.55, 0.4]

imIn = Image.open(inputFileName)
bbox = imIn.getbbox()
inCenter = ((bbox[2] - bbox[0])/2, (bbox[3] - bbox[1])/2)
inSize = max(bbox[2] - bbox[0], bbox[3] - bbox[1])/2
def getInPixel(x, y):
    intX = (int)(inCenter[0] + inSize*x)
    intY = (int)(inCenter[1] + inSize*y)
    if intX >= bbox[0] and intY >= bbox[1] and intX < bbox[2] and intY < bbox[3]:
        return imIn.getpixel((intX, intY))
    else: return (0, 0, 0, 0)

imOut = Image.new(mode, (w, h), bgColor)
draw = ImageDraw.Draw(imOut)

#'''
for k in range(5):
    size = sizes[seq[k]]
    center = (np.sin(np.pi*2*k/5)*mainRadius + w/2, -np.cos(np.pi*2*k/5)*mainRadius + h/2)
    for i in range(-circleRadius + 1, circleRadius):
        for j in range(-circleRadius + 1, circleRadius):
            x = (int)(i + center[0])
            y = (int)(j + center[1])
            if x >= 0 and y >= 0 and x < w and y < h:
                if i**2 + j**2 <= circleRadius**2:
                    draw.point((x, y), circlesColor)
                if i >= -circleRadius*size and i <= circleRadius*size and j >= -circleRadius*size and j <= circleRadius*size:
                    pixel = getInPixel(i/(size*circleRadius), j/(size*circleRadius))
                    if pixel[3] > 100:
                        draw.point((x, y), pixel)
'''

for i in range(w):
    for j in range(h):
        r2 = (i - w/2)**2 + (j - h/2)**2
        if r2 >= (mainRadius - circleRadius)**2 and r2 <= (mainRadius + circleRadius)**2:
            draw.point((i, j), circlesColor)
for k in range(5):
    size = sizes[seq[k]]
    center = (np.sin(np.pi*2*k/5)*mainRadius + w/2, -np.cos(np.pi*2*k/5)*mainRadius + h/2)
    for i in range(-circleRadius + 1, circleRadius):
        for j in range(-circleRadius + 1, circleRadius):
            x = (int)(i + center[0])
            y = (int)(j + center[1])
            if x >= 0 and y >= 0 and x < w and y < h:
                if i >= -circleRadius*size and i <= circleRadius*size and j >= -circleRadius*size and j <= circleRadius*size:
                    pixel = getInPixel(i/(size*circleRadius), j/(size*circleRadius))
                    if pixel[3] > 100:
                        draw.point((x, y), pixel)
'''

imOut.save(outputFileName)