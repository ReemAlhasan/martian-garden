import pygame          # grafik
import blommor         # blommor
import vatten          # regn


bakgrund = pygame.image.load('assets/månen.png')      # bakgrundsbild
ikon = pygame.image.load('assets/hello_world.jpeg')   # ikon


def displayJorden(screen, mode="manual"):
    """Rita månen, regn och blommor."""
    pygame.display.set_icon(ikon)                     # ikon
    pygame.display.set_caption('Självbevattningssystem')  # titel

    screen.blit(bakgrund, (0, 0))                     # rita bakgrunden

    if mode == "manual":                              # manuell bevattning
        vatten.displayVattenManuellt(screen)          # regn med R
        blommor.displayBlommor(screen)                # blommor med R
    elif mode == "auto_system":                       # automatisk bevattning
        vatten.displayVatten(screen)                  # regn alltid
        blommor.displayBlommor_auto(screen)           # auto-cykel
    elif mode == "halv":                              # visa halvvissna
        vatten.displayVatten(screen)
        blommor.display_halvVissnaBlommor(screen)
    elif mode == "friska":                            # visa friska
        vatten.displayVatten(screen)
        blommor.display_friskaBlommor(screen)
    else:                                             # reservläge
        vatten.displayVattenManuellt(screen)
        blommor.displayBlommor(screen)
