#! /bin/bash

[ -d "./public" ] && rm -rf ./public

hugo

rsync -vrP --delete-after ./public/ root@cattette.net:/var/www/cattette
