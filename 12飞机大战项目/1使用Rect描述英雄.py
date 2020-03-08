# -*- coding: utf-8 -*-
# @Time    : 2020/02/16 20:20
# @Author  : xianming yu
# @File    : 1使用Rect描述英雄.py

import pygame
pygame.init()
hero_rect = pygame.Rect(100, 500, 120, 125)
pygame.quit()
print("英雄的原点%d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸%d %d" % (hero_rect.width, hero_rect.height))
print("%d %d"%hero_rect.size) #size是元组属性,也是显示矩形尺寸
