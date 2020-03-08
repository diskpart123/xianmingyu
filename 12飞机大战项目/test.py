# -*- coding: utf-8 -*-
# @Time    : 2020/02/17 19:20
# @Author  : xianming yu
# @File    : test.py

#
# import pygame
#
# pygame.init()
# # 创建游戏窗口
# screen = pygame.display.set_mode((480, 700))
# # 加载游戏背景图像
# bg = pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\background.png")
# # 把图像加载到游戏窗口的指定位置
# screen.blit(bg, (0, 0))
# # 加载英雄飞机图片
# hero = pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\me1.png")
# screen.blit(hero, (200, 300))
# clock = pygame.time.Clock()
# hero_rect = pygame.Rect(200, 300, 102, 126)
#
# while True:
#     clock.tick(1)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("退出游戏")
#             pygame.quit()
#             exit()
#     hero_rect.y -= 10
#     if hero_rect.y <= 0:
#         hero_rect.y = 700
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)
#     pygame.display.update()
# pygame.quit()

class A:
    count=0
    def __init__(self):
        pass

class B(A):
    def __init__(self,name):
        self.name = name
        A.count+=1
nam1=B("yuxianming")
nam2=B("yuxianming1")
print(A.count)