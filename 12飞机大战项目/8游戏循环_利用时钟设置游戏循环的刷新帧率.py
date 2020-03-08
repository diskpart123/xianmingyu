# -*- coding: utf-8 -*-
# @Time    : 2020/02/17 12:52
# @Author  : xianming yu
# @File    : 8游戏循环_利用时钟设置游戏循环的刷新帧率.py

import pygame

pygame.init()
# 创建游戏的窗口 480*700
screen = pygame.display.set_mode((480, 700))
# 绘制图像的三个步骤
# 1.加载背景图像数据
bg = pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\background.png")
# 2.blit绘制图像
screen.blit(bg, (0, 0))
#3.加载英雄图像
hero=pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\me1.png")
#4.blit绘制图像
"""
在PyGame中的坐标原点在左上角(定义的窗口),向右X变大，向左X变小(可为负数),
向下Y变大，向上Y变小(可为负数),下面的(200,300)理解为:x=200,y=500>
"""
screen.blit(hero,(200,300))
# 5.可以在所有绘制工作绘制完成以后,统一调用display.update()方法
pygame.display.update()
#创建时钟对象
clock=pygame.time.Clock()
i=0
#游戏循环->意味着游戏的正式开始
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    print(i)
    i+=1
pygame.quit()
