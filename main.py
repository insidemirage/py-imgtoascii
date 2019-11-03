'''
designed by: Mrage
'''
from PIL import Image, ImageDraw
from colr import Colr as C
import sys
import argparse

'''
resize for std output
'''

def resize_image(img):
    n = 0
    width,height = img.size[0],img.size[1]
    for i in range(1, 10):
        if (width / i < 90):
            n = i
            break
    size = width/n,height/n
    try:
        img.thumbnail(size, Image.ANTIALIAS)
        img.save('tmp.jpg', "JPEG")
    except:
        print("Error with resizing file!")
        sys.exit()
    return Image.open('tmp.jpg')
'''
drawing our image using matrix
'''


def draw_image(width,height,pix):

    for y in range(height):
        for x in range(width):
            r = pix[x,y][0]
            g = pix[x,y][1]
            b = pix[x,y][2]
            print(C().color('s',fore=(r,g,b)),end='')
        print('')

'''
Main loop of the program | bussines only
'''

def main(img):
    image = Image.open(img)
    image = resize_image(image)
    width,height = image.size[0],image.size[1]
    pix = image.load()
    draw_image(width,height,pix)

'''
Gettin' our image path
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert pics to txt')
    parser.add_argument('image',help='Input image')
    args = parser.parse_args()
    main(args.image)


