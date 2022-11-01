import numpy as np
from PIL import Image, ImageDraw

inputFileName = 'C:/Users/79371/Desktop/python apps/psycho/проба.png'
outputFileName = 'C:/Users/79371/Desktop/python apps/psycho/rez.jpg'
w = 512*4
h = 512*4
mode = 'L'
bgColor = 255
mainRadius = (int)(w/2.8)
circlesColor = 210
circleRadius = (int)(w/8.4)
seq = [2, 0, 4, 1, 3]
sizes = [0.7, 1, 1, 1, 1]
sizeShift = 1.3
for i in range(4):
    sizes[i+1] = sizes[i]/sizeShift

imIn = Image.open(inputFileName)
bbox = imIn.getbbox()
inCenter = ((bbox[2] + bbox[0])/2, (bbox[3] + bbox[1])/2)
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
                        draw.point((x, y), (int)((pixel[0] + pixel[1] + pixel[2])/3))
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
#'''

imOut = imOut.resize(((int)(w/4), (int)(h/4)), Image.Resampling.LANCZOS)
imOut.save(outputFileName)