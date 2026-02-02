import pygame
import random

# Ladda in regnbild
rain_img = pygame.image.load("assets/vatten.png")

# Skärmvidd (matcha med din planet!)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Skapa regndroppar
rain_drops = []
for _ in range(10): # ändra här för hur många regndroppar du vill ha!
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(-SCREEN_HEIGHT, 0)
    rain_drops.append([x, y])

def displayVatten(screen):
    for drop in rain_drops:
        drop[1] += 7  # hastighet för regndroppar

        #  Om regndroppar lämnar skärmen, lägg den längst upp
        if drop[1] > SCREEN_HEIGHT:
            drop[1] = random.randint(-100, 0)
            drop[0] = random.randint(0, SCREEN_WIDTH)

        screen.blit(rain_img, (drop[0], drop[1]))
