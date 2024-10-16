# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import *
from constants import *
from asteroid import *
from asteroidfield import *

def main():
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Asteroids game within screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() # asteroids group
    shots = pygame.sprite.Group() # shots group

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable) # shots container

    # Instantiate the Player at the center of the screen
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player_instance = Player(player_x, player_y)

    # Instantiate the asteroid field
    asteroid_field = AsteroidField()

    # Create an instance of Clock & delta time
    clock = pygame.time.Clock() 
    dt = 0

    while 1:
        screen.fill((0, 0, 0)) # Fill the screen with black

        # Update all sprites in the updatable group
        for entity in updatable:
            entity.update(dt)

        # Draw all sprites in the drawable group
        for entity in drawable:
            entity.draw(screen)

        # Collision detection check
        for asteroid in asteroids:
            if player_instance.collision(asteroid):
                print("Game over!")
                sys.exit() # Exit the game loop

        # Collision asteroid with shot check
        for asteroid in list(asteroids):  # Create a copy of the list to safely modify it
            for shot in shots:
                if shot.collision(asteroid):
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(new_asteroids[0])
                        asteroids.add(new_asteroids[1])
                    shot.kill()
                    break  # Break the inner loop as the shot is now gone

        pygame.display.flip() # Update the full display Surface to the screen

        for event in pygame.event.get(): # Iterate over all events in the pygame event queue
            if event.type == pygame.QUIT: # Check if the event is of type QUIT (like clicking 'X' button)
                return # Exit the main game loop, effectively closing the window
        
        dt = clock.tick(60) / 1000 # convert delta time (dt) from milliseconds to seconds, save into dt

if __name__ == "__main__":
    main()