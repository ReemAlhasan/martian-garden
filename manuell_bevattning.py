import pygame
import jorden


pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Manuell bevattning")
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

    # mode="manual": regn + vattning bara när R hålls nere
    jorden.displayJorden(screen, mode="manual")
    pygame.display.update()

pygame.quit()
