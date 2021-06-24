# Funciones y polimorfismo de vectores para asistir al cálculo de movimientos

import math


class vector(object):

    # Polimorfismos

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.vector = (self.x, self.y)

    def __getitem__(self, i):
        return self.vector[i]

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def __add__(self, rhs):  # suma vectorial
        return vector(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):  # resta vectorial
        return vector(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):  # vecor negativo
        return vector(-self.x, -self.y)

    def __mul__(self, scalar):  # miltiplicacion escalar
        return vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):  # division escalar
        return vector(self.x / scalar, self.y / scalar)

    # Métodos

    @staticmethod
    def from_points(p1, p2):  # crea un nuevo vector entre dos puntos
        return vector(p2[0] - p1[0], p2[1] - p1[1])

    def get_magnitude(self):  # módulo del vector
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):  # vector unitario
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
