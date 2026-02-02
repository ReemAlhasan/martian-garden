import pygame

def displayVatten(bakgrund):
    playerImg = pygame.image.load('assets/vatten.png')
    vatten_x = 200 
    vatten_y = 200
    vatten_change = 0
    bakgrund.blit(playerImg, (vatten_x, vatten_y))
