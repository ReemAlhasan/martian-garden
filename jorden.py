import pygame
import vatten

pygame.init()

# Skapa fönster utanför loopen
display = pygame.display.set_mode((1000, 600))
bakgrund = pygame.image.load('assets/jorden.png')
ikon = pygame.image.load('assets/hello_world.jpeg')  # ikonbild (hello world logga)
pygame.display.set_icon(ikon)
pygame.display.set_caption('Självbevattningssystem')

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
    display.fill((0, 0, 0))  # Svart bakgrund
    
    # Rita bilden (t.ex. jorden) på position (0, 0)
    display.blit(bakgrund, (0, 0))
    vatten.displayVatten(display)
    # Uppdatera displayen
    pygame.display.update()

pygame.quit()
