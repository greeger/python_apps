import numpy as np
from PIL import Image, ImageDraw

dirName = 'C:/Users/79371/Desktop/python apps/resize/'

imIn = Image.open(dirName + 'buldiga.png')
for i in [16, 32, 48, 128]:
    imOut = imIn.resize((i, i), Image.Resampling.LANCZOS)
    imOut.save(dirName + 'icon' + (str)(i) + '.png')