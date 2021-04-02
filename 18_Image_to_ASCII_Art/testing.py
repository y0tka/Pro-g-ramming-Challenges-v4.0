from sys import argv
import json
from PIL import Image

symbols = json.load(open("symbs"))
# load symbols list
size = (100, 80)
if len(argv) == 3:
    size = ( int(argv[2]), int((int(argv[2])/5)*4) )
# get right ASCII "image" size

im = Image.open(argv[1]).convert("L").resize(size)
# open image > convert to grayscale > resize to 100x80
px = im.load()
# load picture as set of pixels

output = []
# result list

for y in range(im.size[1]):
    # iterate throu lines
    for x in range(im.size[0]):
        # iterate throu pixels in line
        print(symbols[-px[x,y]//4], end=' ')
        # print symbol that represents a brightness of the pixel
    print("")
    # print the end on line
