import time

import cv2
import numpy as np
from python_imagesearch.imagesearch import imagesearch
# from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, is_retina
import pyautogui

check_x = 1120
check_y = 1320
cross_x = 1480
cross_y = 1340
first_line_top_x = 1140
first_line_top_y = 530
first_line_bottom_x = 1590
first_line_bottom_y = 730


def click_check():
    pyautogui.click(x=check_x, y=check_y)


def click_cross():
    pyautogui.click(x=cross_x, y=cross_y)


# pyautogui.sleep(5)

pyautogui.click(x=first_line_top_x, y=first_line_top_y)

# while True:
#     print(pyautogui.locateOnScreen('1.png'))

ones = pyautogui.locateAllOnScreen('1.png')
#
# for coordinate in ones:
#     print(coordinate)
#
while True:
    time1 = time.time()
    # pos = imagesearcharea("1.png", first_line_top_x, first_line_top_y, first_line_bottom_x, first_line_bottom_y, 0.8)
    #positions = {}
    #for i in range(10):
    # pos = imagesearch("1.png", precision=1)
    coords = imagesearch("1.png")
    # for c in coords:
    #     print(c)
    # if pos[0] != -1:
    #     print("position : ", pos[0], pos[1])
    #     print("TIME ELAPSED:" + str(time.time() - time1) + " seconds")
    #
    # else:
    #     print("image not found")

    print("-------------------------------")
    time.sleep(1)
