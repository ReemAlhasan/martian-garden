import pygame

# Bilder
blommor = pygame.image.load("assets/blommor.png")              # friska blommor
vissnaBlommor = pygame.image.load("assets/blommor_vissna.png") # vissna
halvtVissnaBlommor = pygame.image.load("assets/blommor_halvt_vissna.png")  # halvvissna

# [x, y, fukt]
blommor_list = [
    [50, 420, 10],
    [330, 420, 15],
    [600, 420, 20],
]


def _valj_bild(fukt, frisk_grans, torr_grans):
    if fukt > frisk_grans:
        return blommor
    elif fukt > torr_grans:
        return halvtVissnaBlommor
    else:
        return vissnaBlommor


def displayBlommor(screen):
    """Manuell: R vattnar blommorna."""
    keys = pygame.key.get_pressed()
    vattnar = keys[pygame.K_r]  # True bara när R hålls nere

    FRISK_GRÄNS = 50
    TORR_GRÄNS = 20

    for blomma in blommor_list:
        if vattnar:
            blomma[2] += 2
        else:
            blomma[2] -= 0.3

        # clamp 0–100
        if blomma[2] > 100:
            blomma[2] = 100
        if blomma[2] < 0:
            blomma[2] = 0

        bild = _valj_bild(blomma[2], FRISK_GRÄNS, TORR_GRÄNS)
        screen.blit(bild, (blomma[0], blomma[1]))

def displayBlommor_auto(screen):
    """
    Stabil automatisk bevattning:
    1. Blommorna börjar vissna.
    2. Det regnar tills de är friska.
    3. Regnet stoppas och de torkar långsamt.
    4. När de är vissna igen – börja om.
    """

    # === TRÖSKLAR ===
    TORR_GRANS = 20
    HALV_GRANS = 40
    FRISK_GRANS = 70

    # === INIT STATE FÖRSTA GÅNGEN ===
    if not hasattr(displayBlommor_auto, "state"):
        displayBlommor_auto.state = "VATTNAR"      # Start: regn
        displayBlommor_auto.pause_frames = 0

    # === RÄKNA MEDELFUKT ===
    total = sum([b[2] for b in blommor_list])
    medel = total / len(blommor_list)

    # === STATE MACHINE ===
    if displayBlommor_auto.state == "VATTNAR":
        vattnar = True

        # När de är friska → sluta vattna + aktivera paus
        if medel >= FRISK_GRANS:
            displayBlommor_auto.state = "PAUS"
            displayBlommor_auto.pause_frames = 180  # 3 sekunder vid 60 FPS

    elif displayBlommor_auto.state == "PAUS":
        vattnar = False
        displayBlommor_auto.pause_frames -= 1

        # När pausen är slut börjar de torka
        if displayBlommor_auto.pause_frames <= 0:
            displayBlommor_auto.state = "TORKAR"

    elif displayBlommor_auto.state == "TORKAR":
        vattnar = False

        # när de blir vissna → starta bevattning igen
        if medel <= TORR_GRANS:
            displayBlommor_auto.state = "VATTNAR"

    # === UPPDATERA BLOMMORNAS FUKT ===
    for blomma in blommor_list:
        if vattnar:
            blomma[2] += 0.15    # långsam vattning
        else:
            blomma[2] -= 0.05    # långsam torkning

        blomma[2] = max(0, min(100, blomma[2]))

        # === VÄLJ BILD EFTER FUKT ===
        if blomma[2] >= FRISK_GRANS:
            bild = blommor
        elif blomma[2] >= HALV_GRANS:
            bild = halvtVissnaBlommor
        else:
            bild = vissnaBlommor

        screen.blit(bild, (blomma[0], blomma[1]))

        
def display_halvVissnaBlommor(screen):
    for blomma in blommor_list:
        screen.blit(halvtVissnaBlommor, (blomma[0], blomma[1]))


def display_friskaBlommor(screen):
    for blomma in blommor_list:
        screen.blit(blommor, (blomma[0], blomma[1]))
