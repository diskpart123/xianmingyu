# -*- coding: utf-8 -*-
# @Time    : 2020/02/17 15:56
# @Author  : xianming yu
# @File    : 9游戏循环_英雄动画效果实现.py

#英雄的简单动画实现
"""
需求
    1.在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置
    2.在游戏循环中每次让英雄的y-1做向上移动
    3.y<=0将英雄移动到到屏幕的底部
提示:
    1.每一次调用update()方法之前,需要把所有的游戏图像都重新绘制一遍
    2.而且应该最先重新绘制背景图像
"""

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
screen.blit(hero,(150,300))
# 5.可以在所有绘制工作绘制完成以后,统一调用display.update()方法
pygame.display.update()
#创建时钟对象
clock=pygame.time.Clock()
#定义rect记录飞机的初始位置
hero_rect=pygame.Rect(150,300,102,126)
#游戏循环->意味着游戏的正式开始
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    #修改英雄飞机的位置
    hero_rect.y-=1
    #y<=0将英雄移动到到屏幕的底部
    if hero_rect.y<=0:
        hero_rect.y=700
    #再次绘制游戏背景,避免英雄飞机每次移动有阴影
    screen.blit(bg,(0,0))
    #调用blit方法绘制图像
    screen.blit(hero,hero_rect)
    #调用update()方法更新显示
    pygame.display.update()
pygame.quit()
