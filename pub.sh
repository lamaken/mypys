#!/usr/bin/env bash

#GITSRCPATH="/Users/lamaken/Desktop/docker"
GITSRCPATH="/Users/lamaken/work/src/docker-python-hrznmkr"


cp -rf "image" "$GITSRCPATH/mypys/."
cp -rf "list" "$GITSRCPATH/mypys/."
cp -rf "resources"  "$GITSRCPATH/mypys/."
cp index.html "$GITSRCPATH/mypys/index.html"
cd "$GITSRCPATH"
sh "$GITSRCPATH/help/update_launch.sh"




