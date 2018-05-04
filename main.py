#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  Chaz Bailey
#
# Distributed under terms of the MIT license.

"""
Entrypoint to game

"""

import sys

import pygame
from pygame.locals import *

import objects

# Init pygame
pygame.init()
pygame.key.set_repeat(100, 100)

# Get the game clock
clock = pygame.time.Clock()

# Set a screen up
screen_size = width, height = 500, 500
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('The fish genetic algorithm')

# Create fish
fish_list = []
for i in range(10):
    fish_list.append(objects.Fish())

# Create food
food_list = []
for i in range(10):
    food_list.append(objects.Food())

# define black
white = 255, 255, 255

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Quitting game")
            pygame.quit()
            sys.exit()

    # Start with a blank screen to draw on
    screen.fill(white)

    # Tick the clock
    dt = clock.tick(60)

    # Run the fish
    for fish in fish_list:
        fish.run()
        for food in food_list:
            food.run(fish)

    pygame.display.flip()
