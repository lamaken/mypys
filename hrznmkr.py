# /usr/bin/env python3
# -*- coding: utf-8 -*-


# index points
import random
import uuid

import datetime
from PIL import Image, ImageDraw, ImageFont

CANVAS_NAME = 0
CANVAS_LEFT = 1
CANVAS_TOP = 2
CANVAS_WIDTH = 3
CANVAS_HEIGHT = 4
CANVAS_FILE_NAME = 5
CANVAS_COLOR = 6
#UBU
resources = "/Users/lamaken/PycharmProjects/mypys/resources/"
output = "/Users/lamaken/PycharmProjects/mypys/temp/"

#ferhodinamic POSO NOM DEL L'ARXIU, DATA DE CREACIO
#MAC
#resources = "/Users/lamaken/PycharmProjects/mypys/resources/"
#output = "/Users/lamaken/PycharmProjects/mypys/temp/"
#PROD
#resources = "/var/www/html/mypys/resources/"
#output = "/var/www/html/mypys/temp/"


def random_color():
    levels = range(0, 255, 3)
    return tuple(random.choice(levels) for _ in range(3))


def random_interval(start, end):
    if start == end:
        return start
    if end < start:
        result = random.choice(range(end, start))
    else:
        result = random.choice(range(start, end))
    return result


class Canvas(object):

    def __init__(self, canvas):
        self.name = canvas[CANVAS_NAME]
        self.left = canvas[CANVAS_LEFT]
        self.top = canvas[CANVAS_TOP]
        self.width = canvas[CANVAS_WIDTH]
        self.height = canvas[CANVAS_HEIGHT]
        self.file_name = canvas[CANVAS_FILE_NAME]
        self.color = canvas[CANVAS_COLOR]
        self.signature = self.name, self.left, self.top, self.width, self.height, self.file_name

        print('Canvas ', self.name, 'created')

    def draw_with_rectangles(self, draw):
        img_rectangle = ((self.width - 1, self.height - 1), (self.left + 1, self.top + 1))
        draw.rectangle(img_rectangle, fill=None, outline=(210, 130, 20, 255))

    def draw_with_images(self, hrzimg):
        img_size = (self.width - self.left, self.height - self.top)
        mask = Image.new('RGBA', img_size, self.color)
        image = Image.open(resources + self.file_name).resize(img_size, Image.ANTIALIAS)
        canvas = Image.blend(mask, image, alpha=0.674)
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

        #draw.text((self.width-97, self.height-13),"by hrznmkr ",fill=random_color())

        #mydate = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

        #draw.text((10   , self.height - 13), mydate + " / http://alkasoft.org/mypys/temp/" + self.unik+".png",fill=random_color())
        im.save(self.get_filename())
        im.show()
        del draw

        img_data = open(self.get_filename(), "rb").read()

        return img_data, 'attachment; filename="' + self.unik + '.png"'

    def add(self, another_canvas):
        print "adding another canvas ... _ >> ", another_canvas.signature
        self.allCanvas.append(another_canvas)

    # H.M.T.
    # hand made tests


def genIm():
    BESTIDOR_1_FIGURA = (12, 26)
    BESTIDOR_1_PAISATGE = (22, 14)
    BESTIDOR_1_MARINA = (22, 12)
    # ...
    BESTIDOR_1 = (BESTIDOR_1_FIGURA, BESTIDOR_1_PAISATGE, BESTIDOR_1_MARINA)

    IMAGE_WIDTH = BESTIDOR_1_MARINA[0] *   37
    IMAGE_HEIGHT = BESTIDOR_1_MARINA[1] * 37

    PAL_WIDTH = 13
    PAL_HEIGHT = int(IMAGE_HEIGHT / 4.5)

    # FER UN TEST DE TAMANYS COMPROVAR QUE 100X100 POT SER SI PADING...

    # -- padding
    PADDING_SIZE = (13, 13, 13, 13)

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
    sky_height = int(border[BORDER_HEIGHT] / 1.3)

    # SUN >*<

    SUN_WIDTH = int(sky_height * 1.7145)
    SUN_HEIGHT = int(sky_height * 1.7145)

    SUN_SIZE = (SUN_WIDTH, SUN_HEIGHT)

    # def handler(req):
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

    img_shadow = ("shadow",
                  border[BORDER_LEFT],
                  border[BORDER_TOP] + sky_height,
                  border[BORDER_WIDTH],
                  border[BORDER_HEIGHT],
                  "shadow.png",
                  random_color(),)

    # SUN_POSITION = (border[BORDER_WIDTH] / 2 - SUN_WIDTH / 2, )

    interval_1 = int(border[BORDER_TOP] - SUN_SIZE[1] / 2.5)
    interval_2 = border[BORDER_HEIGHT] - img_land[4] / 2 - SUN_SIZE[1] / 4

    SUN_POSITION = random_interval(interval_1, interval_2)

    interval_1 = -SUN_WIDTH / 2 + border[BORDER_LEFT]
    interval_2 = border[BORDER_WIDTH] - SUN_WIDTH / 2

    print(interval_1, interval_2)

    SOL_RANDOM_LEFT = random_interval(interval_1, interval_2)

    interval_1 = border[BORDER_LEFT] + (IMAGE_WIDTH / 15)
    interval_2 = border[BORDER_WIDTH] - (IMAGE_WIDTH / 15)
    PAL_RANDOM_LEFT = random_interval(interval_1, interval_2)

    PAL_RANDOM_TOP1 = img_sky[4] - PAL_HEIGHT + 3
    PAL_RANDOM_TOP2 = border[BORDER_HEIGHT] - PAL_HEIGHT - (IMAGE_HEIGHT / 20)
    PAL_RANDOM_TOP = random_interval(PAL_RANDOM_TOP1, PAL_RANDOM_TOP2)

    SOL_RANDOM_TOP = SUN_POSITION

    img_sun = ("sun",
               SOL_RANDOM_LEFT,
               SOL_RANDOM_TOP,
               SOL_RANDOM_LEFT + SUN_SIZE[0],
               SOL_RANDOM_TOP + SUN_SIZE[1],
               "sun2.png",
               "orange",)

    img_bara = ("bara",
                PAL_RANDOM_LEFT,
                PAL_RANDOM_TOP,
                PAL_RANDOM_LEFT + PAL_WIDTH,
                PAL_RANDOM_TOP + PAL_HEIGHT,
                "poste.png",
                "brown",)

    # test noms repetits

    if img_bara[1] < SOL_RANDOM_LEFT + SUN_WIDTH / 2:

        img_bara_shadow = ("bara_shadow2",
                           border[BORDER_LEFT] + (IMAGE_WIDTH / 20),
                           img_bara[4] - 5,
                           img_bara[1] + 7,
                           img_bara[4],
                           "bara_shadow_hor.png",
                           "black",)
    else:
        img_bara_shadow = ("bara_shadow1",
                           img_bara[1] + 5,
                           img_bara[4] - 5,
                           border[BORDER_WIDTH] - (IMAGE_WIDTH / 20),
                           img_bara[4],
                           "bara_shadow_hor.png",
                           "black",)

    img_border = ("border",
                  border[BORDER_LEFT] - PADDING_LEFT,
                  border[BORDER_TOP],
                  border[BORDER_WIDTH],
                  border[BORDER_HEIGHT],
                  "border.png",
                  "gold")

    img_lienzo = ("lienzo",
                  border[BORDER_LEFT] - PADDING_LEFT,
                  border[BORDER_TOP],
                  border[BORDER_WIDTH],
                  border[BORDER_HEIGHT],
                  "lienzo.png",
                  (155, 155, 155, 5),)

    img_firma = ("firma",
                  border[BORDER_WIDTH]-120,
                  border[BORDER_HEIGHT]-80,
                  border[BORDER_WIDTH]-50,
                  border[BORDER_HEIGHT]-40,
                  "firma.png",
                  "black",)



    main = MainCanvas(IMAGE_WIDTH, IMAGE_HEIGHT)

    main.add(Canvas(img_sky))
    main.add(Canvas(img_sun))

    main.add(Canvas(img_shadow))
    main.add(Canvas(img_land))

    main.add(Canvas(img_bara_shadow))
    main.add(Canvas(img_bara))

    main.add(Canvas(img_firma))

    main.add(Canvas(img_lienzo))

    main.add(Canvas(img_border))

    return main.draw_canvas()


def handler(req):
    returned_data = genIm()
    req.content_disposition = "attachment; filename=6ce7028b.png";# returned_data[1]
    req.content_type = "image/png"
    req.content_length = str(len(returned_data[0]))
    req.write(returned_data[0])
    return req.OK


print "Only to handle http requests"

hrzmkr_img = genIm()
print hrzmkr_img[1]
hrzmkr_img = genIm()
print hrzmkr_img[1]
hrzmkr_img = genIm()
print hrzmkr_img[1]
hrzmkr_img = genIm()
print hrzmkr_img[1]
hrzmkr_img = genIm()
print hrzmkr_img[1]
hrzmkr_img = genIm()
print hrzmkr_img[1]
hrzmkr_img = genIm()
print hrzmkr_img[1]

