import pygame
import random

rain_img = pygame.image.load("assets/vatten.png")

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

rain_drops = []
for _ in range(10):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(-SCREEN_HEIGHT, 0)
    rain_drops.append([x, y])


def _uppdatera_och_rita(screen, speed):
    for drop in rain_drops:
        drop[1] += speed

        if drop[1] > SCREEN_HEIGHT:
            drop[1] = random.randint(-100, 0)
            drop[0] = random.randint(0, SCREEN_WIDTH)

        screen.blit(rain_img, (drop[0], drop[1]))


def displayVatten(screen):
    """Regn i auto-läge (alltid regn)."""
    _uppdatera_och_rita(screen, speed=3)


def displayVattenManuellt(screen):
    """Regn bara när R hålls nere (manuellt läge)."""
    keys = pygame.key_get_pressed()
    if not keys[pygame.K_r]:
        return
    _uppdatera_och_rita(screen, speed=3)
