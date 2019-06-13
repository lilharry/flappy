# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 20:49:30 2019

@author: Harry Lum
"""

import pygame 
pygame.init()
winLength = 500
winWidth = 600
win = pygame.display.set_mode((winLength, winWidth))
pygame.display.set_caption("Flappy")
skyblue = pygame.Color("#70c5ce")

bird = pygame.transform.scale(pygame.image.load('bird.png'), (50,50))

x = 50
y = 50
accel = 1
run = True
while run:
    pygame.time.delay(10);

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        accel = -6
    print(accel)
    if y + accel <= 0:
        y = 0
    elif y + accel >= winWidth:
        print("true")
        y = winWidth - 40
    else:
        y += accel
    if accel < 40:
        accel += 0.5
    win.fill((0,0,0))
    pygame.draw.rect(win, skyblue, (0, 0, winLength, winWidth * .8))
    win.blit(bird, (x,y))
    
    pygame.display.update()
    
    
pygame.quit()