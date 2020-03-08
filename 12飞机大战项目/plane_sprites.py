# -*- coding: utf-8 -*-
# @Time    : 2020/02/17 20:28
# @Author  : xianming yu
# @File    : plane_sprites.py

"""
本节文档诠释:请看"11pygame快速入门"
"""

import pysnooper
import pygame

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 1.调用父类的初始化方法
        # 在重写初始化方法时，一定要先super()一下父类的方法__init__初始化方法,来保证父类中实现的__init__代码能够被正常执行
        super().__init__()
        # 2.定义对象属性
        self.image = pygame.image.load(image_name)
        # image 的 get_rect() 方法，可以返回 pygame.Rect(0, 0, 图像宽, 图像高) 的对象
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y+=self.speed
