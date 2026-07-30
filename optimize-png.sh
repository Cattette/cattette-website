#!/bin/bash

find ./public -name "*.png" -exec pngquant {} --ext .png --force \;
