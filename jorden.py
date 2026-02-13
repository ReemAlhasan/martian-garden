import pygame
import blommor
import vatten


bakgrund = pygame.image.load('assets/jorden.png')
ikon = pygame.image.load('assets/hello_world.jpeg')


def visaJorden(screen, mode="manual"):
    """Rita jorden, regnet och blommorna beroende på läge."""
    pygame.display.set_icon(ikon)
    pygame.display.set_caption('Självbevattningssystem')

    screen.blit(bakgrund, (0, 0))

    if mode == "manual":                       # manuell bevattning
        vatten.visaVattenManuellt(screen)   # regn bara med R
        blommor.displayBlommor(screen)         # blommor med R
    elif mode == "auto_system":                # automatisk bevattning
        vatten.visaVatten(screen)           # regn alltid
        blommor.displayBlommor_auto(screen)    # auto-cykel
    elif mode == "halv":                       # bara halvvissna
        vatten.visaVatten(screen)
        blommor.display_halvVissnaBlommor(screen)
    elif mode == "friska":                     # bara friska
        vatten.visaVatten(screen)
        blommor.display_friskaBlommor(screen)
    else:                                      # reserv: behandla som manuell
        vatten.visaVattenManuellt(screen)
        blommor.displayBlommor(screen)
