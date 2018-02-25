# /usr/bin/env python3
# -*- coding: utf-8 -*-


# index points
import random
import uuid

from PIL import Image, ImageDraw, ImageFont

resources = "/var/www/html/resources/"
output = "/var/www/html/temp/"



def random_color():
    levels = range(10, 250, 10)
    return tuple(random.choice(levels) for _ in range(3))


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

    def draw_with_rectangles(self, draw):
        img_rectangle = ((self.width - 1, self.height - 1), (self.left + 1, self.top + 1))
        draw.rectangle(img_rectangle, fill=None, outline=(210, 130, 20, 255))

    def draw_with_images(self, hrzimg):
        img_size = (self.width - self.left, self.height - self.top)
        mask = Image.new('RGBA', img_size, self.color)
        image = Image.open(resources + self.file_name).resize(img_size, Image.ANTIALIAS)
        canvas = Image.blend(mask, image, alpha=0.44)
        hrzimg.paste(canvas, (self.left, self.top), image)

    def draw_with_text(self, draw):
        fnt = ImageFont.truetype('/usr/lib/jvm/java-8-oracle/jre/lib/fonts/LucidaSansRegular.ttf', 20)
        draw.text((self.left, self.top), self.name, font=fnt, fill=(255, 255, 255, 220))


class MainCanvas(object):
    def __init__(self, w, h):
        self.allCanvas = []
        self.unik = str(uuid.uuid4())[:8]
        self.height = h
        self.width = w
        self.backcolor = "white"

        print("MainCanvas start.")

    def get_filename(self):
        return output + self.unik + ".png"

    def draw_canvas(self):
        canvas = (self.width, self.height)
        im = Image.new('RGB', canvas, self.backcolor)  # transparent background color
        draw = ImageDraw.Draw(im)

        for index in range(len(self.allCanvas)):
            self.allCanvas[index].draw_with_images(im)
            # self.allCanvas[index].draw_with_rectangles(draw)
            # self.allCanvas[index].draw_with_text(draw)

        im.save(self.get_filename())
        del draw
        data = open(self.get_filename(), "rb").read()
        return data

    def add(self, another_canvas):
        self.allCanvas.append(another_canvas)


# H.M.T.
# hand made tests

IMAGE_WIDTH = 666
IMAGE_HEIGHT = 333

CANVAS_NAME = 0
CANVAS_LEFT = 1
CANVAS_TOP = 2
CANVAS_WIDTH = 3
CANVAS_HEIGHT = 4
CANVAS_FILE_NAME = 5
CANVAS_COLOR = 6

# -- padding
PADDING_SIZE = (33, 33, 33, 33)

PADDING_LEFT = 0
PADDING_TOP = 1
PADDING_RIGHT = 2
PADDING_BOTTOM = 3

BORDER_LEFT = 0
BORDER_TOP = 1
BORDER_WIDTH = 2
BORDER_HEIGHT = 3

border = (PADDING_SIZE[PADDING_LEFT],
          PADDING_SIZE[PADDING_TOP],
          IMAGE_WIDTH - PADDING_SIZE[PADDING_RIGHT],
          IMAGE_HEIGHT - PADDING_SIZE[PADDING_BOTTOM])

# horizon line
sky_height = int(border[BORDER_HEIGHT] * 1 / 1.618033988)

# SUN >*<

SUN_WIDTH = 480
SUN_HEIGHT = 480

SUN_SIZE = (SUN_WIDTH, SUN_HEIGHT)

SUN_POSITION = (border[BORDER_WIDTH] / 2 - SUN_WIDTH / 2, border[BORDER_TOP] + sky_height / 2 - SUN_HEIGHT / 2)



def handler(req):
    img_sky = ("sky",
               border[BORDER_LEFT],
               border[BORDER_TOP],
               border[BORDER_WIDTH],
               border[BORDER_TOP] + sky_height,
               "sky.png",
               random_color(),)

    img_land = ("land",
                border[BORDER_LEFT],
                border[BORDER_TOP] + sky_height,
                border[BORDER_WIDTH],
                border[BORDER_HEIGHT],
                "terrain.png",
                random_color(),)

    img_sun = ("sun",
               SUN_POSITION[0],
               SUN_POSITION[1],
               SUN_POSITION[0] + SUN_SIZE[0],
               SUN_POSITION[1] + SUN_SIZE[1],
               "sun.png",
               random_color(),)

    img_bara = ("bara",
                border[BORDER_WIDTH] - SUN_SIZE[1] / 2 - 5,
                sky_height,
                border[BORDER_WIDTH] - SUN_SIZE[1] / 2,
                sky_height + sky_height / 4,
                "bara.png",
                random_color(),)

    img_bara_shadow = ("shadow",
                       img_bara[1],
                       sky_height + sky_height / 4,
                       img_bara[1] + 105,
                       sky_height + sky_height / 2,
                       "bara_shadow.png",
                       "black",)

    img_border = ("border",
                  border[BORDER_LEFT],
                  border[BORDER_TOP],
                  border[BORDER_WIDTH],
                  border[BORDER_HEIGHT],
                  "border.png",
                  "gold")

    main = MainCanvas(IMAGE_WIDTH, IMAGE_HEIGHT)
    main.add(Canvas(img_sky))
    main.add(Canvas(img_land))
    main.add(Canvas(img_sun))
    main.add(Canvas(img_bara))
    main.add(Canvas(img_bara_shadow))
    main.add(Canvas(img_border))
    data = main.draw_canvas()
    req.content_type = "image/png"
    req.content_length = str(len(data))
    req.write(data)

    return req.OK





