#!/usr/local/bin/python
# -*- coding: UTF-8 -*-


# welcome to hrzmkr.py
# returns an horizon picture

# enable debugging

#fer la classe log/debug


import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import random
import uuid
import os


tempdir = "/var/www/html/temp/"      

def random_color():
	levels = range(10,250,10)
	return tuple(random.choice(levels) for _ in range(3))

def random_pos(m,n):
	r = random.choice(range(m,n))
	return r 

def genImage():
	#horitzontal
	resources = "/var/www/html/resources/"
	param = 1
	
	aureo = param * 1.618033988

	# canvas size
	height = 333#random.choice((100,300,1))
	width = int (height *  aureo)
	skysize     = (width,int((height/ aureo)+1))
	terrainsize = (width,int(height-(height/ aureo)))
	hrzsize     = (width,height)
	sunsize     = (height,height)
	
	# elemens
	#sky
	skypos = (0,0)
	skyColor = random_color()
	sky     = Image.open(resources+"sky.png").resize(skysize , Image.ANTIALIAS)
	skyMasc = Image.new('RGBA', skysize, skyColor)

	#terrain
	terrainpos = (0,int((height/aureo)+1))
	terrainColor = random_color()
	terrain = Image.open(resources+"terrain.png").resize(terrainsize , Image.ANTIALIAS)
	terrainMasc = Image.new('RGBA', terrainsize, terrainColor)

	#terrain shadow
	shadow = Image.open(resources+"shadow.png").resize(terrainsize , Image.ANTIALIAS)
	terrain = Image.blend(terrain,shadow,alpha=0.2)

	#marc
	marc = Image.open(resources+"border.png").resize(hrzsize , Image.ANTIALIAS)
	marcpos = (0,0)

	#sun
	sunpos = (0,0)
	

	sunpos2 = (int(-height/2),int(-height/2))
	randomsunpos = (random_pos(0,width),random_pos(0,int((height/ aureo)+1)))
	

	sunImgpos = tuple(map(sum, zip(sunpos2,randomsunpos)))

	sunColor = random_color()
	sun = Image.open(resources+"sun.png").resize(sunsize , Image.ANTIALIAS)
	sunMasc = Image.new('RGBA', skysize,sunColor)
	sunImg = sun.resize(sunsize)

	#destination 
	hrzimg = Image.new("RGBA",hrzsize,(0,0,0,255))


	sunMasc.paste(sunImg, sunImgpos, sunImg)

	skyImg = Image.blend(skyMasc,sky,alpha=0.80)
	sunImg = Image.blend(skyImg,sunMasc,alpha=0.80)
	terrainImg=Image.blend(terrainMasc,terrain,alpha=0.80)

	skyImg.paste(sunImg,sunpos)
	hrzimg.paste(skyImg,skypos)
	hrzimg.paste(terrainImg,terrainpos,terrainImg)

	
     
	im = ImageDraw.Draw(hrzimg)


     

	#monolito vaya
	

	#bright
	h = height-(height/ aureo)
	tall=random_pos(1,int(h))
	#default len
	y=int((height/ aureo)+1)+random_pos( 0 ,int(height-(height/ aureo))-tall)

	
	palrandompos = ( random_pos(0, width), y) 
	
	#change if far
	#tall = (tall*h)  % (y/h)
	
	

	palpos = tuple(map(sum, zip((0,-tall),palrandompos)))
	im.line((palrandompos,palpos),(200,200,200,200),2)


	#hide
	palpos = tuple(map(sum, zip((1,-tall),palrandompos)))
	palrandompos = tuple(map(sum, zip((1,0),palrandompos)))
	im.line((palpos,palrandompos),(0,0,0,250),2)
	
	#shadow
	shadowX=sunImgpos[0] 

	shadowpos = tuple(map(sum, zip((shadowX,10),palrandompos)))
	im.line( (palrandompos,shadowpos) , (0,0,0,225) , 5 )
	del im

	#ponemos el marco
	hrzimg.paste(marc,marcpos,marc)


		
	#ponemos etiqueta

	unik=str(uuid.uuid4())[:8];

	im = ImageDraw.Draw(hrzimg)
	#im.text((200,y),"y="+str(y),"white")
	#im.text(sunpos2,"*","white")      
	#im.text(palrandompos,"*","white")
	#im.text((200,204),"shadowX="+str(shadowX)+" sunImgpos="+str(sunImgpos[0]),"white")      
	#im.text((200,234),"sunpos="+str(sunpos2[0])+","+str(sunpos2[1]),"white")      
	
	#im.text((100,100),"tall="+str(tall),"white")
	im.text( (width/2-10,height-10),unik,"black")
	im.text( (width/2-10,height-11),unik,"pink")


	im.text( (width-86,height-30)," by hrzmkr","olive")

	im.text( (width-86,height-31)," by hrzmkr","lime")
	
	del im
	
	
	filename=tempdir+unik+".png"
	print filename
	
	hrzimg.save(filename)
	data = open(filename, "rb").read()
	#os.remove(filename)

	return data

def handler(req):
    data = genImage()
    req.content_type = "image/png"
    req.content_length=str(len(data))
    req.write(data)

    return req.OK

print "Only to handle http requests"


"""
nameHrz,
dtHrz,
topHrz,
topHrzColor,
bottomHrzColor,
widthHrz,
heightHrz,
authorHrz,
xPal,yPal,hPalx,hPaly,
alcada,
colPal,
superX,
superY,
version
"""