import pygame          # grafik
import blommor         # blommor
import vatten          # regn


bakgrund = pygame.image.load('bilder/mars.png')       # bakgrund
ikon = pygame.image.load('bilder/hello_world.jpeg')   # ikon

# funktion för att visa planeten Mars 
def visaMars(screen, mode="manual"):
    """Rita bakgrund, regn och blommor."""
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
