import numpy as np
from PIL import Image, ImageDraw

inputDirName = 'C:/Users/79371/Desktop/rez/stN/'
outputDirName = 'C:/Users/79371/Desktop/rez/rez/'
w = 312*4
h = 312*4
mode = 'L'
bgColor = 255
mainRadius = (int)(w/2.8)
circlesColor = 210
circleRadius = (int)(w/8.4)
seq = [[2, 0, 4, 1, 3],
    [0, 4, 1, 3, 2],
    [4, 1, 3, 2, 0],
    [3, 0, 2, 4, 1],
    [2, 3, 1, 0, 4],
    [1, 2, 0, 3, 4],
    [3, 2, 0, 4, 1],
    [1, 3, 2, 0, 4]]
outputNames = ['ts1', 'ts2', 'ts3', 'tn1', 'tn2', 'tn3', 'rs1', 'rs2']
alphabet = ['A', 'B', 'C', 'D', 'E']


#max1=0.7
#min1=0.25
'''qg
k=pow((max1/min1)**2, 0.25)
sizes = [max1**2, 1, 1, 1, 1]
for i in range(4):
    sizes[i+1] = sizes[i]/k
for i in range(5):
    sizes[i] = pow(sizes[i], 0.5)
'''

'''qa
k=(max1**2-min1**2)/4
sizes = [max1**2, 1, 1, 1, 1]
for i in range(4):
    sizes[i+1] = sizes[i]-k
for i in range(5):
    sizes[i] = pow(sizes[i], 0.5)
'''

'''la
k=(max1-min1)/4
sizes = [max1, 1, 1, 1, 1]
for i in range(4):
    sizes[i+1] = sizes[i]-k
'''

'''lg
k=pow(max1/min1, 0.25)
sizes = [max1, 1, 1, 1, 1]
for i in range(4):
    sizes[i+1] = sizes[i]/k
'''


sizes = [0.7, 1, 1, 1, 1]
sizeShift = 1.3
for i in range(4):
    sizes[i+1] = sizes[i]/sizeShift

for st in range(16):
    inputName = 'st' + (str)(st)
    print(inputName)
    imIn = Image.open(inputDirName + inputName + '.png')
    bbox = imIn.getbbox()
    inCenter = ((bbox[2] + bbox[0])/2, (bbox[3] + bbox[1])/2)
    # if st == 6:
    #     inCenter = (inCenter[0], bbox[1] + (bbox[3] - bbox[1])/(1 + np.cos(np.pi/5)))
    inSize = max(bbox[2] - bbox[0], bbox[3] - bbox[1])/2
    r = 0
    for i in range(bbox[0], bbox[2]):
        for j in range(bbox[1], bbox[3]):
            if imIn.getpixel((i, j))[3] > 100:
                currR = (i - inCenter[0])**2 + (j - inCenter[1])**2
                if r**2 < currR:
                    r = np.sqrt(currR)
    def getInPixel(x, y):
        intX = (int)(inCenter[0] + r*x)
        intY = (int)(inCenter[1] + r*y)
        if intX >= bbox[0] and intY >= bbox[1] and intX < bbox[2] and intY < bbox[3]:
            return imIn.getpixel((intX, intY))
        else: return (0, 0, 0, 0)

    for l in range(5):
        imOut = Image.new(mode, (w, h), bgColor)
        draw = ImageDraw.Draw(imOut)
        for k in range(5):
            print(l, ' ', k)
            size = sizes[seq[0][(k-l+2)%5]]
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
                                #draw.point((x, y), (int)((pixel[0] + pixel[1] + pixel[2])/3))
                                draw.point((x, y), 0)

        imOut = imOut.resize(((int)(w/4), (int)(h/4)), Image.Resampling.LANCZOS)
        imOut.save(outputDirName + 'st' + str(st) + alphabet[l] + '.png')
        #imOut.save(outputDirName + inputName + '_' + outputNames[l] + '.jpg')