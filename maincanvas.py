# /usr/bin/env python3
# -*- coding: utf-8 -*-


# index points


class Canvas(object):

    def __init__(self, canvas):
        self.name = canvas[CANVAS_NAME]
        self.left = canvas[CANVAS_LEFT]
        self.top = canvas[CANVAS_TOP]
        self.width = canvas[CANVAS_WIDTH]
        self.height = canvas[CANVAS_HEIGHT]
        self.file_name = canvas[CANVAS_FILE_NAME]
        self.alpha = canvas[CANVAS_ALPHA]

        print('Canvas ', self.name, 'created')


class MainCanvas(object):
    def __init__(self, w, h):
        self.allCanvas = []
        self.height = h
        self.width = w

        print("MainCanvas start.")

    def add(self, another_canvas):
        self.allCanvas.append(another_canvas)

    def draw_rect(self):
        print("MainCanvas draw rect.")







# -- canvas background

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100

SUN_WIDTH = 640
SUN_HEIGHT = 480

SUN_SIZE = (SUN_WIDTH, SUN_HEIGHT)

CANVAS_NAME = 0
CANVAS_LEFT = 1
CANVAS_TOP = 2
CANVAS_WIDTH = 3
CANVAS_HEIGHT = 4
CANVAS_FILE_NAME = 5
CANVAS_ALPHA = 6
CANVAS_COLOR = 7

img_canvas = ("canvas",
              0,
              0,
              IMAGE_WIDTH,
              IMAGE_HEIGHT,
              "background.png",
              255,)

# -- padding


PADDING_SIZE = (20, 20, 20, 20)

PADDING_LEFT = 0
PADDING_TOP = 1
PADDING_BOTTOM = 2
PADDING_RIGHT = 3

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
              255,)

# horizon line
sky_height = border[BORDER_HEIGHT] / 2

img_sky = ("sky",
           border[BORDER_LEFT],
           border[BORDER_TOP],
           border[BORDER_WIDTH],
           sky_height,
           "sky.png",
           255,)

img_land = ("land",
            border[BORDER_LEFT],
            border[BORDER_HEIGHT] - sky_height,
            border[BORDER_WIDTH],
            border[BORDER_HEIGHT],
            "land.png",
            255,)


img_sun = ("sun",
           border[BORDER_LEFT],
           border[BORDER_TOP],
           SUN_SIZE[0],
           SUN_SIZE[1],
           "sun.png",
           255,)

main = MainCanvas(IMAGE_WIDTH, IMAGE_HEIGHT)
main.add(Canvas(img_canvas))
main.add(Canvas(img_padding))
main.add(Canvas(img_border))
main.add(Canvas(img_sky))
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


main.draw_rect()