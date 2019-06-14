# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 20:49:30 2019

@author: Harry Lum
"""

import pygame
import random

rand = random.randint(300, 500)
time = 0
pipePos = 0
pygame.init()
winLength = 500
winWidth = 600
win = pygame.display.set_mode((winLength, winWidth))
pygame.display.set_caption("Flappy")
skyblue = pygame.Color("#70c5ce")
green = pygame.Color("#009600")
impactFont = pygame.font.SysFont("impact", 20)
bird = pygame.transform.scale(pygame.image.load('bird.png'), (50,50))

x = 50
y = 50
accel = 1
run = True
score = 0
pipes = []

while run:
    pygame.time.delay(10);

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        accel = -6

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

    if (time == 1000):
        rand = random.randint(300,500)
        time = 0
        pipePos = 0
        pipes.append({"pipePos": 0, "rand": random.randint(300,500)})
    time += 10

    for pipe in pipes:
        pygame.draw.rect(win, green, (winLength - pipe["pipePos"], 0, 75, pipe["rand"]-200))
        pygame.draw.rect(win, green, (winLength - pipe["pipePos"], pipe["rand"], 75, winWidth))
        pipe["pipePos"] += 2
        if pipe["pipePos"] == 450:
            score += 1
        if ((x + 40 > (winLength - pipe["pipePos"])) and (x < (winLength - pipe["pipePos"] + 75))):
            if ((y + 10 < pipe["rand"] - 200) or (y + 20 > pipe["rand"])):
                run = False

    win.blit(bird, (x,y))

    text = impactFont.render("Score: " + str(score), True, (255, 255, 255))
    #get rect dimensions of text for centering purposes

    win.blit(text, (winLength /2 - text.get_rect().width/2, 50))

    pygame.display.update()






pygame.quit()
