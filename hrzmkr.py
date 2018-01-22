#!/usr/local/bin/python
# -*- coding: UTF-8 -*-


# welcome to hrzmkr.py
# returns an horizon picture

# enable debugging


import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import random
import uuid
import os


tempdir = "/var/www/html/temp/"      

def random_color():
      levels = range(10,150,10)
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
      height = 637#random.choice((100,300,1))
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
      terrain = Image.blend(terrain,shadow,alpha=0.5)

      #marc
      marc = Image.open(resources+"border.png").resize(hrzsize , Image.ANTIALIAS)
      marcpos = (0,0)

      #sun
      sunpos = (0,0)
      

      sunpos2 = (int(-height/2.3),int(-height/2.3))
      randomsunpos = (random_pos(0,width),random_pos(0,int((height/ aureo)+1)))
      

      sunImgpos = tuple(map(sum, zip(sunpos2,randomsunpos)))
      print sunImgpos

      sunColor = random_color()
      sun = Image.open(resources+"sun.png").resize(sunsize , Image.ANTIALIAS)
      sunMasc = Image.new('RGBA', skysize,sunColor)
      sunImg = sun.resize(sunsize)

      #destination 
      hrzimg = Image.new("RGBA",hrzsize,(0,0,0,255))

      #sombra pal pseudo ANTIALIAS
      sombrapal = Image.new("RGBA",hrzsize,(0,0,0,5))
      im = ImageDraw.Draw(sombrapal)
      im.line((width/2+1,height*0.73,width*0.8,height*0.78),(0,0,0,225),5)

     

      del im
      sombrapal=sombrapal.resize((width-(width/3),height-(height/3)),Image.ANTIALIAS)
      sombrapal=sombrapal.resize((width,height),Image.ANTIALIAS)

      sunMasc.paste(sunImg, sunImgpos, sunImg)

      skyImg = Image.blend(skyMasc,sky,alpha=0.50)
      sunImg = Image.blend(skyImg,sunMasc,alpha=0.50)
      terrainImg=Image.blend(terrainMasc,terrain,alpha=0.50)

      skyImg.paste(sunImg,sunpos)
      hrzimg.paste(skyImg,skypos)
      hrzimg.paste(terrainImg,terrainpos,terrainImg)
      hrzimg.paste(sombrapal,sunpos,sombrapal)

      #palo monolito vaya
      im = ImageDraw.Draw(hrzimg)


      palrandompos = ( random_pos(10, width), int((height/ aureo)+1)+random_pos( 0 ,int(height-(height/ aureo)))) 
      print palrandompos

      im.line(palrandompos,(180,180,180,255),2)


      im.line((width/2, height*0.55,width/2,height*0.73),(220,200,200,205),3)
      im.line((width/2+1, height*0.55,width/2+1,height*0.73),(0,0,0,205),2)
      del im

      #ponemos el marco
      hrzimg.paste(marc,marcpos,marc)

      #ponemos etiqueta
      im = ImageDraw.Draw(hrzimg)
      #im.text(sunImgpos,"*","white")      
      #im.text(palrandompos,"|","white")


      #del im
      
     
      filename=tempdir+str(uuid.uuid4())+".png"
      print filename
      
      hrzimg.save(filename)
      data = open(filename, "rb").read()
      os.remove(filename)

      return data

def handler(req):
    data = genImage()
    req.content_type = "image/png"
    req.content_length=str(len(data))
    req.write(data)

    return req.OK
