import sys

import pygame

from backend import *
from computer_sounds import SOUNDS

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600

# Set up colors
GREEN = (44, 174, 107)
YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)

# # Set up the font
font_path = "eurostile.TTF"
font_size = 24

font = pygame.font.Font(font_path, font_size)
# Make the font bold
# font.set_bold(True)

# Set up the input box
input_box = pygame.Rect(100, 100, 600, 50)
color_active = pygame.Color('dodgerblue2')
INPUT_BOX_COLOR = (200, 200, 200)
MAX_WIDTH = 500
active = True
text = ''

# Output variables
output_text = ''

# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Smart Computer")

humSound = SOUNDS["hum"]
humSound.play(loops=-1)
humVolume = humSound.get_volume()


# Function to handle command execution
def execute_command(command):
    return computer(message=command)


def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    output_text = execute_command(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Fill the window with white color
    window.fill(GREEN)

    # Render the input box and text
    pygame.draw.rect(window, INPUT_BOX_COLOR, input_box)
    pygame.draw.rect(window, color_active, input_box, 2)
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    renderTextCenteredAt(output_text, font, YELLOW, 400, 200, window, 600)

    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
