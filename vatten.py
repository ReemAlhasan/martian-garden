import pygame

def displayVatten(bakgrund):
    vatten = pygame.image.load('assets/vatten.png')
    vatten_x = 200 
    vatten_y = 200
    vatten_change = 0
    bakgrund.blit(vatten, (vatten_x, vatten_y))
