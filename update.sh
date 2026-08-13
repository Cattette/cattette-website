#! /bin/bash

[ -d "./public" ] && rm -rf ./public

hugo

rsync -vruP --delete-after ./public/ root@cattette.net:/var/www/cattette
