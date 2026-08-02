#!/bin/bash

# lossy compression
find ./public -name "*.png" -exec pngquant {} --ext .png --force \; &&
# balls to the walls lossless compression
find ./public -name "*.png" -exec oxipng -o max -Z --fix {} \; 
