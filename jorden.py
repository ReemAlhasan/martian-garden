import pygame
import vatten

pygame.init()

# Skapa fönster
display = pygame.display.set_mode((1000, 600))

bakgrund = pygame.image.load('assets/jorden.png')
ikon = pygame.image.load('assets/hello_world.jpeg')

pygame.display.set_icon(ikon)
pygame.display.set_caption('Självbevattningssystem')

clock = pygame.time.Clock()
running = True

while running:
   # clock.tick(60)  # limitera FPS (frames per second) - redigera denna (minska) om du har problem med prestandan!

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Måla bakgrund
    display.fill((0, 0, 0))
    display.blit(bakgrund, (0, 0))

    # Måla regn 
    vatten.displayVatten(display)

    pygame.display.update()

pygame.quit()
