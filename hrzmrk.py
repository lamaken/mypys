#!/usr/bin/env python

import PIL.Image as Image


#horitzontal

resources = "resources/"
param = 1
aureo = param * 1.618033988


# canvas size
height = 291
width = int (height *  aureo)
skysize 	= (width,int((height/ aureo)+1))
terrainsize = (width,int(height-(height/ aureo)))
hrzsize		= (width,height)
sunsize 	=  skysize


# elements

sky 	= Image.open(resources+"sky.png").resize(skysize , Image.ANTIALIAS)
terrain = Image.open(resources+"terrain.png").resize(terrainsize , Image.ANTIALIAS)
sun	= Image.open(resources+"sun.png").resize(sunsize , Image.ANTIALIAS)


# filter colors

mascaraR	= Image.open(resources+"red.png").resize(hrzsize , Image.ANTIALIAS)
mascaraG	= Image.open(resources+"green.png").resize(hrzsize , Image.ANTIALIAS)
mascaraB	= Image.open(resources+"blue.png").resize(hrzsize , Image.ANTIALIAS)


#destination 

hrzimg 	= Image.open(resources+"blanco.png").resize(hrzsize , Image.ANTIALIAS)

skypos = (0,0)
terrainpos = (0,int((height/aureo)+1))
sunpos = (0,0)

hrzimg.paste(sky, skypos, sky)
hrzimg.paste(sun, sunpos, sun)
hrzimg.paste(terrain, terrainpos, terrain)


# blend with alpha=0.5
result = Image.blend(hrzimg, hrzimg, alpha=0.5)

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
hrzimg.save('hrz3.gif')
hrzimg.show()
