""" Objects module to hold all the objects for the game
"""

import random

import pygame
from pygame.locals import *

import utils
from neural import NeuralNetwork


class Fish(object):
    """ A fish
    """
    TURN_SPEED = 0.2
    ACCELERATION_AMOUNT = 1
    MAX_SPEED = 10
    MIN_SPEED = 0

    def __init__(self):
        self.surface = pygame.image.load("fish.bmp")
        self.rotated_surface = self.surface
        self.rectangle = self.surface.get_rect()
        self.speed = 1
        self.x = random.randint(1, pygame.display.get_surface().get_width())
        self.y = random.randint(1, pygame.display.get_surface().get_width())
        self.direction = random.randint(1, 360)
        self.fitness = 0
        self.neural_network = NeuralNetwork()

    def run(self):
        """ The main method for the fish, should be run each game tick
        """

        self.__handle_events()

        # Rotate the fish
        self.__rotate()

        # Move the fish
        self.__move()

        # Draw the fish
        pygame.display.get_surface().blit(self.rotated_surface, self.rectangle)

    def __move(self):
        dx, dy = utils.vector_to_delta_speed(self.direction, self.speed)
        self.x += dx
        self.y += dy
        if self.x > pygame.display.get_surface().get_width():
            self.x = pygame.display.get_surface().get_width()
        if self.x < 0:
            self.x = 0
        if self.y > pygame.display.get_surface().get_height():
            self.y = pygame.display.get_surface().get_height()
        if self.y < 0:
            self.y = 0
        self.rectangle.x = round(self.x)
        self.rectangle.y = round(self.y)
        self.rectangle.clamp_ip(pygame.display.get_surface().get_rect())

    def __rotate(self):
        self.rotated_surface = pygame.transform.rotate(self.surface, utils.rads_to_degrees(self.direction))

    def __accelerate(self):
        """ Accelerate the fish
        """
        if self.speed < self.MAX_SPEED:
            self.speed += self.ACCELERATION_AMOUNT

    def __decelerate(self):
        """ Decelerate the fish
        """
        if self.speed > self.MIN_SPEED:
            self.speed -= self.ACCELERATION_AMOUNT

    def __turn_left(self):
        self.direction += self.TURN_SPEED

    def __turn_right(self):
        self.direction -= self.TURN_SPEED

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.__accelerate()
                if event.key == K_s:
                    self.__decelerate()
                if event.key == K_a:
                    self.__turn_left()
                if event.key == K_d:
                    self.__turn_right()


class Food(object):
    def __init__(self):
        self.surface = pygame.image.load("food.bmp")
        self.rectangle = self.surface.get_rect()
        self.rectangle.x = random.randint(1, pygame.display.get_surface().get_width())
        self.rectangle.y = random.randint(1, pygame.display.get_surface().get_height())

    def run(self, fish):
        if fish.rectangle.colliderect(self.rectangle):
            self.get_eaten(fish)

        pygame.display.get_surface().blit(self.surface, self.rectangle)

    def get_eaten(self, fish):
        fish.fitness += 1
        self.__init__()
