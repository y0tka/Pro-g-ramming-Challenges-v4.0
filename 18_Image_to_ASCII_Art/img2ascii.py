import sys
import json
from PIL import Image


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("""Usage:
    python img2ascii.py [FILE] [SIZE]
    FILE - path to the file
    SIZE - number of output lines (80 by default)
""")
    sys.exit()

symbols = json.load(open("symbs"))
# load symbols list

size = (100, 80)
if len(sys.argv) == 3:
    size = ( int(sys.argv[2]), int((int(sys.argv[2])/5)*4) )
# get right ASCII "image" size or 100x80 by default

im = Image.open(sys.argv[1]).convert("L").resize(size)
# open image > convert to grayscale > resize to 100x80
px = im.load()
# load picture as set of pixels

output = []
# result will be stored here

for y in range(im.size[1]):
    # iterate throu lines
    for x in range(im.size[0]):
        # iterate throu pixels in line
        print(symbols[-px[x,y]//4], end=' ')
        # print symbol that represents a brightness of the pixel
    print("")
    # print the end on line
