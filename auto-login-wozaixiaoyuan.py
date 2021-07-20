import pyautogui
import time

# 根据已有图像a获取屏幕上识别到的图像a到坐标
def pressImgCen(imgDir):
    status = pyautogui.locateCenterOnScreen(imgDir, grayscale=False, confidence=0.7)
    print(status, imgDir)
    count = 1
    # 防止识别失败，识别失败返回None，判断接受到的是否为元组，重试
    while (count < 20) and (status == None):
        print("识别失败，结果为：", status , "，暂停1s后重试")
        count+=1
        time.sleep(0.5)
        status = pyautogui.locateCenterOnScreen(imgDir, grayscale=False, confidence=0.7)
    #点击坐标
    if status != None:
        x,y = status
        pyautogui.click(x, y, duration=0.3)


# 鼠标位置初始化
pyautogui.moveTo(2477, 18, duration=0.3)
time.sleep(0.1)

# 自动登录微信并且打卡
pyautogui.press('winleft')

pressImgCen("./auto-click/weixin.png")
pressImgCen("./auto-click/weixin-login.png")
pressImgCen("./auto-click/phone-wx-login.png")
pressImgCen("./auto-click/wzxy.png")
pressImgCen("./auto-click/xsd.png")
pressImgCen("./auto-click/Allow.png")
pressImgCen("./auto-click/health-daka.png")
pressImgCen("./auto-click/get-position.png")
# 鼠标滚轮下拉，防止提交按钮出不来
time.sleep(0.5)
pyautogui.scroll(-50)
# 下拉要时间，等等
print("鼠标滚轮下拉等待1s")
time.sleep(1)
pressImgCen("./auto-click/take-in.png")
pressImgCen("./auto-click/queren.png")
pressImgCen("./auto-click/off-wzxy.png")
pressImgCen("./auto-click/off-wx.png")
