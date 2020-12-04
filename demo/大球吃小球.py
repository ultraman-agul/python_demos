# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/29 12:22
# Software : PyCharm
# version： Python 3.7
# @File    : 大球吃小球.py
# description :

import pygame

def main():
    # 初始化
    pygame.init()
    # 窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 窗口标题
    pygame.display.set_caption('大球吃小球')
    # 窗口背景色
    screen.fill((242, 242, 242))
    # 绘制一个圆
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if '__name__' == '__main__':
    main()