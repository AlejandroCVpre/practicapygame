import pygame
import math
from sys import exit

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

# -------- carga imagenes ---------
image = pygame.Surface((32, 32))
original_image = image.copy()
poligono = pygame.draw.polygon(image, pygame.Color('dodgerblue'), ((0, 0), (32, 16), (0, 32)))
rect = image.get_rect(center=((100, 100)))
posicion = (300, 300)

# -------------- variables iniciales -------------
angulo = 0
direccion = pygame.Vector2(1, 0)


# ------------- funciones ----------------

def calc_angulo(origen, destino):
    dist_x = destino[0] - origen[0]
    dist_y = destino[1] - origen[1]
    return math.degrees(math.atan2(-dist_y, dist_x))


def calc_direccion(angulo):
    return pygame.Vector2(1, 0).rotate(-angulo)


def pos_mouse():
    mouse = pygame.mouse.get_pos()
    return mouse


# -------------- main loop -------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mouse_xy = pos_mouse()
    angulo = calc_angulo(posicion, mouse_xy)
    print(angulo)

    # Dibujar pantalla
    screen = pygame.display.set_mode((1024, 768), 0, 32)

    player_image = pygame.transform.rotate(image, angulo)
    player_rect = player_image.get_rect()
    player_rect.center = posicion
    screen.blit(player_image, player_rect)

    pygame.display.update()
    # pygame.display.flip() solo hace update de una porcion
