import os
import time

import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import win32api, win32con

k = PyKeyboard()
m = PyMouse()


# 匹配图片相似度
def dingwei(sh_img, tar_img):
    # sh_img 截图 tar_img 辨识图
    sh_img_data = cv2.imread(sh_img, 0)
    tar_img_data = cv2.imread(tar_img, 0)

    threshold = 0.95  # 匹配度
    gps = []
    res = cv2.matchTemplate(sh_img_data, tar_img_data, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)    
    for pt in zip(*loc[::-1]):
        gps.append(pt)
    #print(gps)
    return gps


# 截图检测登陆界面
def screenshot_login():
    bbox = (0, 0, 1000, 500)
    im = ImageGrab.grab(bbox)
    im.save('login.png')
    return 'login.png'


# 截图战网登陆按钮
def screenshot_bnet():
    bbox = (0, 0, win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
    im = ImageGrab.grab(bbox)
    im.save('bnet.png')
    return 'bnet.png'


def start_check():
    login_img = screenshot_login()
    gps = dingwei(login_img, '1.png')
    os.remove(login_img)
    k.tap_key(k.space_key) 
    if len(gps) > 0:
        # 切换
        print('检测登陆界面，匹配成功')
        k.press_key(k.alt_key)
        k.tap_key(k.function_keys[4])
        k.release_key(k.alt_key)

        k.press_key(k.alt_key)
        k.tap_key(k.tab_key)
        k.release_key(k.alt_key)
        print('切换')
        time.sleep(1)
        bnet_img = screenshot_bnet()
        gps = dingwei(bnet_img, '2.png')
        os.remove(bnet_img)
        if len(gps) > 0:
            print('检测战网登陆界面，匹配成功')
            for (x, y) in gps:
                m.click(int(x) + 50, int(y) + 50, 1)
                print('点击登陆')
                time.sleep(30)
                k.tap_key(k.enter_key)         


if __name__ == '__main__':
    while True:
        start_check()
        time.sleep(10)
