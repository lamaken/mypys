# /usr/bin/env python3
# -*- coding: utf-8 -*-

# UBU

resources = "/var/www/html/resources/"
output = "/var/www/html/out/"
webpath = "http://localhost/out/"
# ferhodinamic POSO NOM DEL L'ARXIU, DATA DE CREACIO
# MAC
# resources = "/Users/lamaken/PycharmProjects/mypys/resources/"
# output = "/Users/lamaken/PycharmProjects/mypys/list/"
# PROD
# resources = "/var/www/html/mypys/resources/"
# output = "/var/www/html/mypys/list/"



import os, os.path


def list_images():
    imgs = []
    valid_images = [".png"]
    for f in os.listdir(output):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(webpath, f))
    return imgs


def handler(req):
    #returned_data = list_images()
    returned_data = ("alex.png","josep.png")
    req.content_type = "text/html"
    out = ""

    if len(returned_data) == 0:
        out = "<center>No images have found!</center>"
    else:
        for i in returned_data:
         out += i+","

    req.content_length = str(len(out))
    req.write(out)

    return req.OK



