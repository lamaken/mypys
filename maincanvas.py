# /usr/bin/env python3
# -*- coding: utf-8 -*-


# index points
from random import random

from PIL import Image, ImageDraw, ImageFont


class Canvas(object):

    def __init__(self, canvas):
        self.name = canvas[CANVAS_NAME]
        self.left = canvas[CANVAS_LEFT]
        self.top = canvas[CANVAS_TOP]
        self.width = canvas[CANVAS_WIDTH]
        self.height = canvas[CANVAS_HEIGHT]
        self.file_name = canvas[CANVAS_FILE_NAME]
        self.color = canvas[CANVAS_COLOR]

        print('Canvas ', self.name, 'created')

    def draw_it(self, draw):
        # rectangles (width, height, left position, top position)
        img_rectangle = ((self.width, self.height), (self.left, self.top))
        #img_rectangle = ((self.left, self.height), (self.width, self.height))

        # draw rectangle
        draw.rectangle(img_rectangle, fill=self.color, outline=(0,0,0,255))
        fnt = ImageFont.truetype('/usr/lib/jvm/java-8-oracle/jre/lib/fonts/LucidaSansRegular.ttf', 20)
        draw.text((self.left, self.top), self.name, font=fnt, fill=(255, 255, 255, 220))
#        draw.text((self.left, self.top), (self.width, self.height), self.name)


class MainCanvas(object):
    def __init__(self, w, h):
        self.allCanvas = []
        self.height = h
        self.width = w
        self.backcolor = (0, 0, 0, 255)

        print("MainCanvas start.")

    def draw_canvas(self):
        canvas = (self.width, self.height)
        im = Image.new('RGBA', canvas, self.backcolor)  # transparent background color
        draw = ImageDraw.Draw(im)

        for index in range(len(self.allCanvas)):
            self.allCanvas[index].draw_it(draw)

        #im.save('/home/alex/PycharmProjects/mypys/temp/im.png')
        del draw
        im.show()

    def add(self, another_canvas):
        self.allCanvas.append(another_canvas)


# H.M.T.
# hand made tests

IMAGE_WIDTH = 600
IMAGE_HEIGHT = 300

CANVAS_NAME = 0
CANVAS_LEFT = 1
CANVAS_TOP = 2
CANVAS_WIDTH = 3
CANVAS_HEIGHT = 4
CANVAS_FILE_NAME = 5
CANVAS_COLOR = 6

img_canvas = ("canvas",
              0,
              0,
              IMAGE_WIDTH,
              IMAGE_HEIGHT,
              "background.png",
              25,)

# -- padding



PADDING_SIZE = (30, 30, 30, 30)

PADDING_LEFT = 0
PADDING_TOP = 1
PADDING_RIGHT = 2
PADDING_BOTTOM = 3

img_padding = ("padding",
               int(img_canvas[CANVAS_LEFT] + PADDING_SIZE[PADDING_LEFT]),
               int(img_canvas[CANVAS_TOP] + PADDING_SIZE[PADDING_TOP]),
               int(img_canvas[CANVAS_WIDTH] - PADDING_SIZE[PADDING_RIGHT]),
               int(img_canvas[CANVAS_HEIGHT] - PADDING_SIZE[PADDING_BOTTOM]),
               "padding.png",
               255,)

BORDER_LEFT = 0
BORDER_TOP = 1
BORDER_WIDTH = 2
BORDER_HEIGHT = 3

border = (img_padding[CANVAS_LEFT],
          img_padding[CANVAS_TOP],
          img_padding[CANVAS_WIDTH],
          img_padding[CANVAS_HEIGHT])

img_border = ("border",
              border[BORDER_LEFT],
              border[BORDER_TOP],
              border[BORDER_WIDTH],
              border[BORDER_HEIGHT],
              "marc.png",
              "green",)

# horizon line
sky_height = border[BORDER_HEIGHT] / 2

img_sky = ("sky",
           border[BORDER_LEFT],
           border[BORDER_TOP],
           border[BORDER_WIDTH],
           border[BORDER_TOP]+sky_height,
           "sky.png",
           "blue",)

img_land = ("land",
            border[BORDER_LEFT],
            border[BORDER_TOP] + sky_height,
            border[BORDER_WIDTH],
            border[BORDER_HEIGHT],
            "land.png",
            "brown",)

# SUN >*<

SUN_WIDTH = 80
SUN_HEIGHT = 80

SUN_SIZE = (SUN_WIDTH, SUN_HEIGHT)

SUN_POSITION = (border[BORDER_WIDTH] / 2 - SUN_WIDTH / 2, border[BORDER_TOP] + sky_height / 2)

img_sun = ("sun",
           SUN_POSITION[0],
           SUN_POSITION[1],
           SUN_POSITION[0]+SUN_SIZE[0],
           SUN_POSITION[1]+SUN_SIZE[1],
           "sun.png",
           "yellow",)

main = MainCanvas(IMAGE_WIDTH, IMAGE_HEIGHT)
main.add(Canvas(img_canvas))
main.add(Canvas(img_padding))
main.add(Canvas(img_border))
main.add(Canvas(img_sky))
main.add(Canvas(img_land))
main.add(Canvas(img_sun))

print "1. canvas"
print img_canvas
print "2. padding"
print img_padding
print "3. border"
print img_border
print "4. sky"
print img_sky
print "5. land"
print img_land
print "6. sun"
print img_sun

main.draw_canvas()
