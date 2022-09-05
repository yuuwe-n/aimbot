#!/bin/python3

import cv2 as cv
import numpy as np
from time import time
import pyautogui

img = cv.imread('test_image.png',0)
img2 = img.copy()

template = cv.imread('plus.png',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

result = cv.matchTemplate(img, template, cv.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

top_left = max_loc
print(top_left)

bottom_right = (top_left[0] + w, top_left[1] + h)
center = (top_left[0] + w/2, top_left[1] + h/2)
print(center)
print(bottom_right)

cv.rectangle(img,top_left, bottom_right, 255, 2)

pyautogui.moveTo(center)

