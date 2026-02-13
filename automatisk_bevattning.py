import pygame
import jorden # här importerar vi klassen jorden så att vi kan använda den 


pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Automatisk bevattning")
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    jorden.visaJorden(screen, mode="auto_system") # här visar vi jorden
    pygame.display.update()

pygame.quit()
