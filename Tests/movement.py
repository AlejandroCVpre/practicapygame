import pygame
import math
from vectores import *
from pygame.locals import *

pygame.init()


# La funcion de esta clase es actualizar los valores de coordenada y rotacion con los imputs
class movimiento(object):

    def __init__(self, spawn, speed):
        self.coordenada = spawn
        self.vector_speed = vector(speed, speed)
        self.speed = speed
        self.angulo = 0

    # Para procesar de forma eficiente, el clock lo debe llevar el módulo que llame a las funciones de movimiento,
    # de otra forma se ralentiza mucho. Por eso se añade el argumento time_passed_seconds en escena.py.

    # Movimiento por teclado
    def movimiento_player(self, time_passed_seconds):  # velocidad, x e y iniciales
        pressed_keys = pygame.key.get_pressed()  # devuelve teclas apretadas
        key_direction = vector(0, 0)  # vector unitario recipiente

        if pressed_keys[K_a]:  # se actualiza el vector unitario con las teclas presionadas
            key_direction.x = -1
        elif pressed_keys[K_d]:
            key_direction.x = +1
        if pressed_keys[K_w]:
            key_direction.y = -1
        elif pressed_keys[K_s]:
            key_direction.y = +1

        self.coordenada += key_direction * self.speed * time_passed_seconds  # actualiza la posicion
        return self.coordenada

    # rebota entre las coordenadas
    def rebote(self, time_passed_seconds):
        if self.coordenada.x > 1024:
            self.vector_speed.x = -self.vector_speed.x
        elif self.coordenada.x < 0:
            self.vector_speed.x = -self.vector_speed.x
        if self.coordenada.y > 768:
            self.vector_speed.y = -self.vector_speed.y
        elif self.coordenada.y < 0:
            self.vector_speed.y = -self.vector_speed.y

        self.coordenada.x += self.vector_speed.x * time_passed_seconds
        self.coordenada.y += self.vector_speed.y * time_passed_seconds
        return self.coordenada

    # Persigue la posición del atributo "punto"
    def hacia_punto(self, punto, time_passed_seconds):
        destination = punto
        position = self.coordenada
        heading = vector.from_points(position, destination)
        heading.normalize()  # se obtiene la direccion

        self.coordenada += heading * self.speed * time_passed_seconds
        return self.coordenada

    def rotacion_mouse(self):
        mouse = pygame.mouse.get_pos()
        pos_obj_x, pos_obj_y = self.coordenada.x, self.coordenada.y
        dist_x, dist_y = pos_obj_x - mouse[0], pos_obj_y - mouse[1]
        self.angulo = math.degrees(math.atan2(-dist_y, dist_x))
        return self.angulo

    @staticmethod
    def rotacion_mouse_static(pos_mouse, coordenada_inicial):
        mouse = pos_mouse
        pos_obj_x, pos_obj_y = coordenada_inicial.x, coordenada_inicial.y
        dist_x, dist_y = pos_obj_x - mouse[0], pos_obj_y - mouse[1]
        angulo = math.degrees(math.atan2(-dist_y, dist_x))
        return angulo

    def calc_direccion(self):
        x = 1 * math.cos(self.angulo)
        y = 1 * math.sin(self.angulo)
        return vector(x, y)

    def lineal(self, direccion, time_passed_seconds):
        self.coordenada += direccion * self.speed * time_passed_seconds
        return self.coordenada
