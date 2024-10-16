import pygame
import circleshape
import constants
import random

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
        self.position += self.velocity * dt # Move the asteroid based on its velocity
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return None
        
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        new_asteroid1.velocity = new_velocity1
        new_asteroid2.velocity = new_velocity2

        return new_asteroid1, new_asteroid2