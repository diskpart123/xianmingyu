# -*- coding: utf-8 -*-
# @Time    : 2020/02/17 17:00
# @Author  : xianming yu
# @File    : 10事件监听_基本概念和event模块的get方法.py

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
hero_rect=pygame.Rect(150,300,200,126)
#游戏循环->意味着游戏的正式开始
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    #捕获监听事件
    for event in pygame.event.get():
        #判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出....")
            #调用quit()方法卸载所有模块
            pygame.quit()
            #在调用exit()方法,直接终止当前执行的程序
            exit()
    # event_list=pygame.event.get()
    # if len(event_list)>=0:
    #     print(event_list)
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



