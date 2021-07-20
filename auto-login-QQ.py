import pyautogui
import time

pyautogui.press('winleft')

def pressImgCen(imgDir):
    status = pyautogui.locateCenterOnScreen(imgDir, grayscale=False, confidence=0.7)
    print(status, imgDir)
    count = 1
    # 防止识别失败，识别失败返回None，判断接受到的是否为None
    while (count < 20) and (status == None):
        print("识别失败，结果为：", status , "，暂停0.5s后重试")
        count+=1
        time.sleep(0.5)
        status = pyautogui.locateCenterOnScreen(imgDir, grayscale=False, confidence=0.7)
    #点击坐标
    if status != None:
        x,y = status
        pyautogui.click(x, y, duration=0.5)

# 尝试自动登录qq
pressImgCen("./auto-click/qq.png")
pressImgCen("./auto-click/qqLogin.png")