# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 14:26
# @Author  : xianming yu
# @File    : 25对角线移动.py

import win32gui
import win32con
import  time
qq=win32gui.FindWindow("TXGuiFoundation","QQ")
while True:
    for size in range(0, 800, 10):  # 如果让放大速度慢一点,可以把步长10,改成1
        win32gui.SetWindowPos(qq,  # 操作qq
                              win32con.HWND_TOPMOST,  # 最上方
                              size,  # 位置x
                              size * 768 // 1080,  # 位置y    修改对角线的位置
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW
                              )
        for size in range(800,0,-10): #如果让缩小速度慢一点,可以把步长-10,改成-1
            win32gui.SetWindowPos(qq,  #操作qq
                                  win32con.HWND_TOPMOST, #最上方
                                  size, #位置x
                                  size * 768//1080, #位置y    修改对角线的位置
                                  300,#长度
                                  300,#宽度
                                  win32con.SWP_SHOWWINDOW
                                  )

