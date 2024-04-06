import pygame

pygame.mixer.init(44100, -16, 2, 2048)
MINHUMVOL = 0.7
MAXHUMVOL = 1.0
SOUNDS = {
    "hum": pygame.mixer.Sound('Crisis_Theme.mp3'),
}
SOUNDS["hum"].set_volume(MINHUMVOL)
