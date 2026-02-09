import pygame
import blommor
import vatten


bakgrund = pygame.image.load('assets/jorden.png')
ikon = pygame.image.load('assets/hello_world.jpeg')


def displayJorden(screen, mode="manual"):
    """Rita jorden, regnet och blommorna beroende på läge."""
    pygame.display.set_icon(ikon)
    pygame.display.set_caption('Självbevattningssystem')

    screen.blit(bakgrund, (0, 0))

    if mode == "manual":                       # manuell bevattning
        vatten.displayVattenManuellt(screen)   # regn bara med R
        blommor.displayBlommor(screen)         # blommor med R
    elif mode == "auto_system":                # automatisk bevattning
        vatten.displayVatten(screen)           # regn alltid
        blommor.displayBlommor_auto(screen)    # auto-cykel
    elif mode == "halv":                       # bara halvvissna
        vatten.displayVatten(screen)
        blommor.display_halvVissnaBlommor(screen)
    elif mode == "friska":                     # bara friska
        vatten.displayVatten(screen)
        blommor.display_friskaBlommor(screen)
    else:                                      # reserv: behandla som manuell
        vatten.displayVattenManuellt(screen)
        blommor.displayBlommor(screen)
