#!/usr/bin/env python

from PIL import Image


#horitzontal

param = 1
aureo = param * 1.618033988


height = 291


width = int (height *  aureo)





skysize 	= (width,int((height/ aureo)+1))
terrainsize = (width,int(height-(height/ aureo)))
hrzsize		= (width,height)
sunsize 	=  skysize

sky 	= Image.open("sky.png").resize(skysize , Image.ANTIALIAS)
terrain = Image.open("terrain.png").resize(terrainsize , Image.ANTIALIAS)
hrzimg 	= Image.open("blanco.png").resize(hrzsize , Image.ANTIALIAS)
sun	= Image.open("sun.png").resize(sunsize , Image.ANTIALIAS)

tempimg=terrain.copy()


skypos = (0,0)
terrainpos = (0,int((height/aureo)+1))
sunpos = (20,0)

hrzimg.paste(sky, skypos, sky)
hrzimg.paste(sun, sunpos, sun)
hrzimg.paste(terrain, terrainpos, terrain)

hrzimg.save('hrz3.gif')
hrzimg.show()
"""
creo la mascara de color per a tot el dibuix



sky = Image.open('sky.png')

sun = Image.open('sun.png')
sunResized = sun.resize(140, 140)

image = sky.copy()
position = (10,10)
image.paste(sunResized, position, sunResized)
image_copy.save('hrz2.png')
"""