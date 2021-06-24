from movement import *

pygame.init()


class player(movimiento):

    def __init__(self, time_passed_secods):
        self.sprite_filename = "imagenes/pngegg.png"  # carga la imagen
        self.spawn_player = vector(100, 100)  # lugar en el que aparece por primera vez, coordenada inicial
        self.speed_player = 10  # velociad de movimiento
        self.time_counter = time_passed_secods
        self.bullet_speed = 5

        movimiento.__init__(self, self.spawn_player, self.speed_player)
        self.heading = movimiento.calc_direccion(self)

    def update(self):
        movimiento.movimiento_player(self, time_passed_seconds=self.time_counter)
        movimiento.rotacion_mouse(self)

