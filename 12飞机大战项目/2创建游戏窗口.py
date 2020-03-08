# -*- coding: utf-8 -*-
# @Time    : 2020/02/16 20:22
# @Author  : xianming yu
# @File    : 2创建游戏窗口.py

import pygame
pygame.init()
# 创建游戏的窗口 480*700
"""
执行后程序会返回一个黑色窗口,但是不一会就会消失,为了不让黑窗口消失,
我们在下面一行添加一个while死循环保持黑窗口一直显示
"""
screen = pygame.display.set_mode((480,700))
while True:
    pass
pygame.quit()
