# /usr/bin/env python3
# -*- coding: utf-8 -*-

# ferhodinamic POSO NOM DEL L'ARXIU, DATA DE CREACIO
# MAC
# resources = "/Users/lamaken/PycharmProjects/mypys/resources/"
# output = "/Users/lamaken/PycharmProjects/mypys/list/"
# PROD
# resources = "/var/www/html/mypys/resources/"
# output = "/var/www/html/mypys/list/"
from mod_python import apache
import os


output = "/var/www/html/mypys/out/"
webpath = "http://localhost:8888/mypys/out/"


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
    returned_data = list_images()
    req.content_type = "text/plain"
    out = ""
    if len(returned_data) == 0:
        out = webpath
    else:
        for i in returned_data:
            out += i + ","
    req.write(out)
    return apache.OK


print "Only to handle http requests"
