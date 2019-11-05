'''
designed by: Mrage
modded with <3 by: Vaker
depends on: Image, Colr, numpy
'''
from PIL import Image, ImageDraw
from colr import Colr as C
import numpy as np
import sys, argparse

'''
average tile brightness
'''
def getAvgBrightness(image):
    im = np.array(image.convert('L'))
    w,h = im.shape
    return np.average(im.reshape(w*h))

'''
average tile color
'''
def getAvgColor(image):
    im = np.array(image)
    return np.mean(im, axis=(0, 1))

'''
drawing our image using matrix
'''
def draw_image(cols,rows,tileH,tileW,pix):
    whiteToBlack = '@%#*+=-:. '
    width,height = pix.size[0],pix.size[1]

    for y in range(cols):
        yStart = int(y*tileH)
        yEnd = int((y+1)*tileH)

        if y == cols-1:
            yEnd = height

        for x in range(rows):
            xStart = int(x*tileW)
            xEnd = int((x+1)*tileW)

            if x == rows-1:
                xEnd = width

            tile = pix.crop((xStart, yStart, xEnd, yEnd))

            lum = 255 - int(getAvgBrightness(tile))
            clr = getAvgColor(tile)

            char = whiteToBlack[int((lum*9)/255)]
            print(C().color(char,fore=(clr[0],clr[1],clr[2])),end='')
        print('')

'''
Main loop of the program | business only
'''
def main(image, cols, debug):
    image = Image.open(image)
    width,height = image.size[0],image.size[1]

    #tile size calculation
    tileW = width/cols
    tileH = tileW/0.43 #width/height scale for characters
    rows = int(height/tileH) #resulting rows count

    if cols > width or rows > height:
        print("Image too small, check --cols argument!")
        exit(0)
    if debug:
        print("Image size {}x{}".format(width, height))
        print("Tile size {}x{}".format(tileW, tileH))
        print("{} cols, {} rows".format(cols, rows))

    draw_image(rows,cols,tileH,tileW,image)

'''
Gettin' our image path
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert pics to txt')
    parser.add_argument('image',help='Input image')
    parser.add_argument('--cols',dest='cols',default=80,const=80,nargs='?',type=int,help='Cols amount',required=False)
    parser.add_argument('--showinfo',dest='show_info',help='Show info before image',action='store_true')
    args = parser.parse_args()
    main(args.image, args.cols, args.show_info)
