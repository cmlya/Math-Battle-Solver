import time

import cv2
import numpy as np
from python_imagesearch.imagesearch import imagesearch_v2, imagesearcharea
import pyautogui
from PIL import Image

check_x = 1120
check_y = 1450
cross_x = 1480
cross_y = 1450
first_line_top_x = 1000
first_line_top_y = 500
first_line_bottom_x = 1590
first_line_bottom_y = 715
second_line_x = 1800
second_line_y = 900

prompt_bounds = (
    first_line_top_x,
    first_line_top_y,
    second_line_x,
    second_line_y
)

templates = [cv2.imread(f"{i}.png", 0) for i in range(10)]
operators = {op: cv2.imread(f"{op}.png", 0) for op in ["+", "-", "x", "div"]}

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


pyautogui.sleep(5)
while True:
    time1 = time.time()
    nums = {}
    res = {}
    for i in range(10):
        coords = imagesearcharea(
            templates[i],
            *prompt_bounds
        )
        # coords = imagesearch(f"{i}.png")
        print(len(coords))
        for coord in coords:
            if coord[1] > first_line_bottom_y:
                res[coord[0]] = i
            else:
                nums[coord[0]] = i

    for op, op_template in operators.items():
        prec = 0.95 if op == "*" else 0.8
        coords = imagesearcharea(
            op_template,
            *prompt_bounds,
            precision=prec
        )
        if len(coords) == 0:
            continue
        nums[coords[0][0]] = {
            "+": "+",
            "-": "-",
            "x": "*",
            "div": "/"
        }[op]
        break

    print("nums: " + str(nums))
    print("res: " + str(res))
    expression = ""
    for i in sorted(nums.keys()):
        expression += str(nums.get(i))
        # print(i, end="")
    result = ""
    for i in sorted(res.keys()):
        result += str(res.get(i))
    print("getting result", result)
    result = int(result)

    print(expression)
    print("= " + str(result))

    if "+" in expression:
        split = expression.split("+")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " + " + str(x2))
        print("result: " + str(result))
        is_correct = x1 + x2 == result
        print("is correct: ", str(is_correct), f"({x1} + {x2} == {result})")
        if x1 + x2 == result:
            click_check()
        else:
            click_cross()

    elif "-" in expression:
        split = expression.split("-")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " - " + str(x2))
        print("result: " + str(result))
        is_correct = x1 - x2 == result
        print("is correct: ", str(is_correct), f"({x1} - {x2} == {result})")
        if x1 - x2 == result:
            click_check()
        else:
            click_cross()

    elif "*" in expression:
        split = expression.split("*")
        x1 = int(split[0])
        x2 = int(split[1])
        print("x1, x2:" + str(x1) + " * " + str(x2))
        print("result: " + str(result))
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
        print("result: " + str(result))
        is_correct = x1 / x2 == result
        print("is correct: " + str(is_correct))
        if x1 / x2 == result:
            click_check()
        else:
            click_cross()

    print("TIME ELAPSED:" + str(time.time() - time1) + " seconds")
    print("-------------------------------")
