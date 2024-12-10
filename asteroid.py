from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        rad = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, rad)
        ast_1.velocity = self.velocity.rotate(angle) * 1.2
        ast_2 = Asteroid(self.position.x, self.position.y, rad)
        ast_2.velocity = self.velocity.rotate(angle) * -1.2