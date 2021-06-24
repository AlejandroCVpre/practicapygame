from movement import *

pygame.init()


class player(movimiento):

    def __init__(self):
        self.sprite_filename = "imagenes/pngegg.png"  # carga la imagen
        self.spawn_player = vector(100, 100)  # lugar en el que aparece por primera vez, coordenada inicial
        self.speed_player = 10  # velociad de movimiento
        self.bullet_speed = 15

        movimiento.__init__(self, self.spawn_player, self.speed_player)

    def update(self, time_passed_seconds):
        movimiento.movimiento_player(self, time_passed_seconds)
        movimiento.rotacion_mouse(self)

