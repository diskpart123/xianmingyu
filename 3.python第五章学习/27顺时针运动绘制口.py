# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 15:15
# @Author  : xianming yu
# @File    : 27顺时针运动绘制口.py

import win32gui
import win32con
import time
import math

qq = win32gui.FindWindow("TXGuiFoundation", "QQ")
while True:
    for size in range(0, 800, 10):  # 如果让放大速度慢一点,可以把步长10,改成1
        win32gui.SetWindowPos(qq,  # 操作qq
                              win32con.HWND_TOPMOST,  # 最上方
                              size,  # 位置x
                              0,  # 位置y    修改对角线的位置
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW
                              )
    for size in range(0, 600, 10):  # 如果让放大速度慢一点,可以把步长10,改成1
        win32gui.SetWindowPos(qq,  # 操作qq
                              win32con.HWND_TOPMOST,  # 最上方
                              800,  # 位置x
                              size,  # 位置y    修改对角线的位置
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW
                              )
    for size in range(800, 0, -10):  # 如果让放大速度慢一点,可以把步长10,改成1
        win32gui.SetWindowPos(qq,  # 操作qq
                              win32con.HWND_TOPMOST,  # 最上方
                              size,  # 位置x
                              600,  # 位置y    修改对角线的位置
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW
                              )
    for size in range(600, 0, -10):  # 如果让放大速度慢一点,可以把步长10,改成1
        win32gui.SetWindowPos(qq,  # 操作qq
                              win32con.HWND_TOPMOST,  # 最上方
                              0,  # 位置x
                              size,  # 位置y    修改对角线的位置
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW
                              )
