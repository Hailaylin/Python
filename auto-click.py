#   图像识别或者其它方式获取要模拟点击的坐标，然后模拟人点击
#   主要想用于我在校园自动打卡

import pyautogui


# 获取坐标
x,y=pyautogui.position()
print(x,y)

# 获取屏幕尺寸
print(pyautogui.size())

#   移动鼠标
# pyautogui.moveTo(100, 100, duration=0.7)

#   移动鼠标到图片坐标中点点击
# print( pyautogui.locateCenterOnScreen("./auto-click/down.png"))
# print(x,y)

# pyautogui.click(x, y, duration=0.7)

# 尝试操作一波自动打开QQ微信
import win32.win32gui
import win32.win32api
import win32.win32console
import time

# pyautogui.press('winleft')

# # 根据已有图像a获取屏幕上识别到的图像a到坐标
# def pressImgCen(imgDir):
#     status = pyautogui.locateCenterOnScreen(imgDir, grayscale=False, confidence=0.7)
#     print(status)
#     # 防止识别失败，识别失败返回None，判断接受到的是否为元组，重试
#     while status == None:
#         print("识别失败，结果为：", status , "，暂停两秒后重试")
#         time.sleep(2)
#         status = pyautogui.locateCenterOnScreen(imgDir, grayscale=False, confidence=0.7)
#     #点击坐标
#     x,y = status
#     pyautogui.click(x, y, duration=0.7)

# # 尝试自动登录qq
# pressImgCen("./auto-click/qq.png")
# pressImgCen("./auto-click/qqLogin.png")

