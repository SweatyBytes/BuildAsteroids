# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while 1 == 1:
        screen.fill((0, 0, 0)) # Fill the screen with black
        pygame.display.flip() # Update the full display Surface to the screen

        for event in pygame.event.get(): # Iterate over all events in the pygame event queue
            if event.type == pygame.QUIT: # Check if the event is of type QUIT (like clicking 'X' button)
                return # Exit the main game loop, effectively closing the window

if __name__ == "__main__":
    main()