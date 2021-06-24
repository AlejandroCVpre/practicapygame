import pygame
from movement import *
from pygame.locals import *
from sys import exit
from vectores import *

pygame.init()


class enemy(movimiento):

    def __init__(self):
        self.sprite_enemy = "imagenes/derp.jpg"  # carga la imagen
        self.spawn_enemy = vector(600, 400)  # lugar en el que aparece por primera vez, coordenada inicial
        self.speed_enemy = 5  # velociad de movimiento

        movimiento.__init__(self, self.spawn_enemy, self.speed_enemy)  # movimiento necesita
        # coordenada de spawn
