import pygame
import os
import time
import random

class Jorden(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/assets/jorden.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect(center=(400, 450))
        self.moisture = 100
        self.plant_alive = True
        self.last_water = time.time()
        self.water_offset = 0  # För rörligt vatten

    def update(self):
        if time.time() - self.last_water > 15:
            self.moisture -= random.uniform(1, 3)
            if self.moisture < 20:
                self.dodr_blomma()
        else:
            self.moisture = 100
        self.water_offset += 2  # Animera vatten

    def dodr_blomma(self):
        if self.plant_alive:
            self.plant_alive = False
            print("Blomman dog på Jorden!")  # Eller byt sprite

    def bevatta(self):
        self.last_water = time.time()
