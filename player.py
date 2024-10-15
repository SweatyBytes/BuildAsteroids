import pygame
import circleshape
import constants

class Player(circleshape.CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # If the 'a' key is pressed, turn left
            self.rotate(-dt)

        if keys[pygame.K_d]: # If the 'd' key is pressed, turn right
            self.rotate(dt)
        
        if keys[pygame.K_w]:  # If the 'W' key is pressed, move forward
            self.move(dt)

        if keys[pygame.K_s]:  # If the 'S' key is pressed, move backward
            self.move(-dt)  # Reverse direction by using -dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt