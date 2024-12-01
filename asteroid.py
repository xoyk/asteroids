from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroidA = Asteroid(self.position.x, self.position.y, new_radius)
            asteroidB = Asteroid(self.position.x, self.position.y, new_radius)
            asteroidA.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroidB.velocity = self.velocity.rotate(-random_angle) * 1.2
            self.kill()
