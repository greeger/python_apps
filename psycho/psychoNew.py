import numpy as np
from PIL import Image, ImageDraw

inputDirName = 'C:/Users/79371/Desktop/rez/stN/'
outputDirName = 'C:/Users/79371/Desktop/rez/rez/345/'
w = 312*4
h = 312*4
mode = 'L'
bgColor = 255
mainRadius = (int)(w/2.8)
circlesColor = 210
circleRadius = (int)(w/8.4)
seq = [[4, 2, 5, 3, 1],
    [3, 4, 2, 5, 1],
    [5, 3, 2, 4, 1],
    [4, 5, 2, 3, 1],
    [2, 4, 5, 3, 1],

    [2, 0, 4, 1, 3],
    ]
for i in range(5):
    for j in range(5):
        seq[i][j] = 5 - seq[i][j]
alphabet = ['A', 'B', 'C', 'D', 'E']

seqNum = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
for i in range(10):
    seqNum[i] -= 1
seqAlpha = [1, 2, 1, 3, 2, 3, 4, 4, 0, 0]
def getSize(index):
    currSeq = seq[seqNum[index]]
    minInd = 0
    while True:
        if currSeq[minInd] == 4:
            break
        minInd += 1
    newSeq = [0, 0, 0, 0, 0]
    for i in range(5):
        newSeq[i] = currSeq[(i-seqAlpha[index]+minInd)%5]
    return newSeq


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

schem = 0
for st in [3, 4, 6, 7, 8, 9, 10, 12, 13, 15]:
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

    imOut = Image.new(mode, (w, h), bgColor)
    draw = ImageDraw.Draw(imOut)
    currSizes = getSize(schem)
    for k in range(5):
        print(k)
        size = sizes[currSizes[k]]
        center = (np.sin(np.pi*2*k/5)*mainRadius + w/2, -np.cos(np.pi*2*k/5)*mainRadius + h/2)
        for i in range(-circleRadius + 1, circleRadius):
            for j in range(-circleRadius + 1, circleRadius):
                x = (int)(i + center[0])
                y = (int)(j + center[1])
                if x >= 0 and y >= 0 and x < w and y < h:
                    if i**2 + j**2 <= circleRadius**2:
                        draw.point((x, y), circlesColor)
                    if currSizes[k] <= 2 and i >= -circleRadius*size and i <= circleRadius*size and j >= -circleRadius*size and j <= circleRadius*size:
                        pixel = getInPixel(i/(size*circleRadius), j/(size*circleRadius))
                        if pixel[3] > 100:
                            #draw.point((x, y), (int)((pixel[0] + pixel[1] + pixel[2])/3))
                            draw.point((x, y), 0)

    imOut = imOut.resize(((int)(w/4), (int)(h/4)), Image.Resampling.LANCZOS)
    imOut.save(outputDirName + 'st' + str(st) + '_345s.png')
    schem += 1
