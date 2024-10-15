import pygame
import circleshape
# import constants # not sure if we need this yet.

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, 
                       (255, 255, 255),  # White color
                       self.position,
                       self.radius,
                       2)
    
    def update(self, dt):
        # Move the asteroid based on its velocity
        self.position += self.velocity * dt