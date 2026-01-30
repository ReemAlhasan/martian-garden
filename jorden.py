import pygame
import vatten

pygame.init()

# Skapa fönster utanför loopen
bakgrund = pygame.display.set_mode((1000, 600))
playerImg = pygame.image.load('C:/Users/reema/Documents/KlimatStudio/assets/jorden.png')
ikon = pygame.image.load("C:/Users/reema/Documents/KlimatStudio/assets/helloWorld.png")  # ikonbild (hello world logga)
pygame.display.set_icon(ikon)
pygame.display.set_caption("Självbevattningssystem")

running = True
while running:
    # Hantera events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Rita bakgrunden (svart som standard, eller fyll med färg om du vill)
    bakgrund.fill((0, 0, 0))  # Svart bakgrund
    
    # Rita bilden (t.ex. jorden) på position (0, 0)
    bakgrund.blit(playerImg, (0, 0))
    vatten.displayVatten(bakgrund)
    # Uppdatera displayen
    pygame.display.update()

pygame.quit()
