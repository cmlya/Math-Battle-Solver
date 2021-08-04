import time

import cv2
import numpy as np
from python_imagesearch.imagesearch import imagesearch, imagesearcharea
import pyautogui
from PIL import Image

check_x = 1120
check_y = 1450
cross_x = 1480
cross_y = 1450
# first_line_top_x = 1140
# first_line_top_y = 530
# first_line_bottom_x = 1590
first_line_bottom_y = 730


# check_x = imagesearch("check.png")[0][0]
# check_y = imagesearch("check.png")[0][1]
# cross_x = imagesearch("wrong.png")[0][0]
# cross_y = imagesearch("wrong.png")[0][1]
# second_line_y = imagesearch("=.png")[0][1]

# zero_w = Image.open("0.png").width
# one_w = Image.open("1.png").width
# two_w = Image.open("2.png").width
# three_w = Image.open("3.png").width
# four_w = Image.open("4.png").width
# five_w = Image.open("5.png").width
# six_w = Image.open("6.png").width
# seven_w = Image.open("7.png").width
# eight_w = Image.open("8.png").width
# nine_w = Image.open("9.png").width


def click_check():
    print("CORRECT")
    pyautogui.click(x=check_x, y=check_y)


def click_cross():
    print("INCORRECT")
    pyautogui.click(x=cross_x, y=cross_y)


pyautogui.sleep(1)
while True:
    time1 = time.time()
    # pos = imagesearcharea("1.png", first_line_top_x, first_line_top_y, first_line_bottom_x, first_line_bottom_y)
    nums = {}
    res = {}
    coords = imagesearch("0.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 0
        else:
            nums[coord[0]] = 0
    coords = imagesearch("1.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 1
        else:
            nums[coord[0]] = 1
    coords = imagesearch("2.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 2
        else:
            nums[coord[0]] = 2
    coords = imagesearch("3.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 3
        else:
            nums[coord[0]] = 3
    coords = imagesearch("4.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 4
        else:
            nums[coord[0]] = 4
    coords = imagesearch("5.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 5
        else:
            nums[coord[0]] = 5
    coords = imagesearch("6.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 6
        else:
            nums[coord[0]] = 6
    coords = imagesearch("7.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 7
        else:
            nums[coord[0]] = 7
    coords = imagesearch("8.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 8
        else:
            nums[coord[0]] = 8
    coords = imagesearch("9.png")
    for coord in coords:
        if coord[1] > first_line_bottom_y:
            res[coord[0]] = 9
        else:
            nums[coord[0]] = 9
    found_operation = False
    while not found_operation:
        coords = imagesearch("+.png")
        if len(coords) != 0:
            nums[coords[0][0]] = "+"
            found_operation = True
            continue
        coords = imagesearch("-.png")
        if len(coords) != 0:
            nums[coords[0][0]] = "-"
            found_operation = True
            continue
        coords = imagesearch("x.png", precision=0.95)
        if len(coords) != 0:
            nums[coords[0][0]] = "*"
            found_operation = True
            continue
        coords = imagesearch("div.png")
        nums[coords[0][0]] = "/"
        found_operation = True
        continue

    print("nums: " + str(nums))
    expression = ""
    for i in sorted(nums.keys()):
        expression += str(nums.get(i))
        # print(i, end="")
    result = ""
    for i in sorted(res.keys()):
        result += str(res.get(i))

    print(expression)
    print("= " + result)

    if "+" in expression:
        split = expression.split("+")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " + " + str(x2))
        print("result: " + result)
        is_correct = x1 + x2 == result
        print("is correct: " + str(is_correct))
        if x1 + x2 == result:
            click_check()
        else:
            click_cross()

    elif "-" in expression:
        split = expression.split("-")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " - " + str(x2))
        print("result: " + result)
        is_correct = x1 - x2 == result
        print("is correct: " + str(is_correct))
        if x1 - x2 == result:
            click_check()
        else:
            click_cross()

    elif "*" in expression:
        split = expression.split("*")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " * " + str(x2))
        print("result: " + result)
        is_correct = x1 * x2 == result
        print("is correct: " + str(is_correct))
        if x1 * x2 == result:
            click_check()
        else:
            click_cross()

    elif "/" in expression:
        split = expression.split("/")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " / " + str(x2))
        print("result: " + result)
        is_correct = x1 / x2 == result
        print("is correct: " + str(is_correct))
        if x1 / x2 == result:
            click_check()
        else:
            click_cross()

    print("TIME ELAPSED:" + str(time.time() - time1) + " seconds")
    print("-------------------------------")
    # time.sleep(1)
