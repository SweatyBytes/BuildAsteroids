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
            self.move(-dt)

        if keys[pygame.K_SPACE]:  # If the 'Spacebar' key is pressed, shoot a shot
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        shot_position = self.position
        shot_velocity = pygame.Vector2(0, -1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        new_shot = Shot(shot_position.x, shot_position.y, constants.SHOT_RADIUS)
        new_shot.velocity = shot_velocity
        self.groups()[0].add(new_shot)  # Add the new shot to the same group as the player


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity
    
    def draw(self, surface):
        pygame.draw.circle(surface, 
                       (255, 255, 255),  # White color
                       self.position,
                       self.radius,
                       2)
    
    def update(self, dt):
        # Move the shot based on its velocity
        self.position += self.velocity * dt
