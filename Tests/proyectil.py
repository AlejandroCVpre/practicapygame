from movement import *

pygame.init()


class proyectil(movimiento):

    def __init__(self, spawn, velocidad):
        self.coordenada = spawn
        self.angulo = 0
        self.speed_bala = velocidad
        self.image = pygame.Surface((8, 8))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color('orange'), (4, 4), 4)

        movimiento.__init__(self, self.coordenada, self.speed_bala)

    def update(self, time_passed_seconds):
        self.coordenada.x += self.speed_bala.x * time_passed_seconds
        self.coordenada.y += self.speed_bala.y * time_passed_seconds
