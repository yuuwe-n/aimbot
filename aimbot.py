#!/bin/python3

'''
pip install numpy opencv-python pyautogui Pillow
'''

import time

import cv2
import mss
import numpy
import pyautogui

#pyautogui.moveTo(100,100)
#pyautogui.click()

template = cv2.imread('plus.png',0)

def match(screenshot, template):
    w, h = template.shape[::-1]

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    top_left = max_loc
    print(top_left)
    
    bottom_right = (top_left[0] + w, top_left[1] + h)
    center = (top_left[0] + w/2, top_left[1] + h/2)
    return(center)


# start game button found using pyautogui.cursor()
pyautogui.moveTo(958,265,2)
pyautogui.click()

start_time = time.time()

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

    while time.time() - start_time < 20:
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        screenshot = numpy.array(sct.grab(monitor))

        # Display the picture
        #cv2.imshow("OpenCV/Numpy normal", screenshot)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2GRAY)
        x, y = match(screenshot, template) 
        pyautogui.moveTo(x, y)
        pyautogui.click()

        print("fps: {}".format(1 / (time.time() - last_time)))



