# klass för vatten
import pygame
import random

#bild på vattendroppar
rain_img = pygame.image.load("bilder/vatten.png")

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# skapa regndroppar
rain_drops = []
for _ in range(10): # <-- skapar såhär många vattendroppar!
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(-SCREEN_HEIGHT, 0)
    rain_drops.append([x, y])

# måla vattendroppar på skärmen
def _uppdatera_och_rita(screen, speed):
    for drop in rain_drops:
        drop[1] += speed

        if drop[1] > SCREEN_HEIGHT:
            drop[1] = random.randint(-100, 0)
            drop[0] = random.randint(0, SCREEN_WIDTH)

        screen.blit(rain_img, (drop[0], drop[1]))

# visa vatten på skärmen 
def visaVatten(screen):
    """Regn i auto-läge (alltid regn)."""
    _uppdatera_och_rita(screen, speed=3) # <-- ändra snabbhet på dropparna här!

# visar vatten manuellt genom att hålla in v för vatten
def visaVattenManuellt(screen):
    """Regn bara när R hålls nere (manuellt läge)."""
    keys = pygame.key.get_pressed()
    if not keys[pygame.K_v]:
        return
    _uppdatera_och_rita(screen, speed=3) # <-- ändra snabbhet på dropparna här!
