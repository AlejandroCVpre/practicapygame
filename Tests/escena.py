import math

import pygame
from player import *
from proyectil import *
from pygame.locals import *
from sys import exit

pygame.init()

# Clock
clock = pygame.time.Clock()  # lleva cuenta del tiempo
time_passed = clock.tick(30)  # 1 tick = 1 ms, parametro = fps
time_passed_seconds = time_passed / 1000

# Creacion de objetos
nave = player(time_passed_seconds)
vel_bala = 5

# Carga de fondo e imagenes
screen = pygame.display.set_mode((1024, 768), 0, 32)  # Tamaño de la ventana
sprite = pygame.image.load(nave.sprite_filename).convert_alpha()
background = pygame.image.load('imagenes/meme.jpg').convert()

# Main loop, llama las funciones que calculan las coordenadas de los elementos y los dibuja en pantalla. Las coordenadas
# de los elementos se guardan en el objeto, se llama con "objeto.coordenada.x o y"

balas = []
pos_mouse = 0
while True:
    screen.blit(background, (0, 0))
    nave.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance_x = mouse_x - nave.coordenada.x
            distance_y = mouse_y - nave.coordenada.y
            angle = math.atan2(distance_y, distance_x)
            speed_x = 5 * math.cos(angle)
            speed_y = 5 * math.sin(angle)
            velocidad = vector(speed_x, speed_y)
            balas.append(proyectil(nave.coordenada, velocidad))

    for b in balas:
        b.update(time_passed_seconds)
        screen.blit(b.image, (b.coordenada.x, b.coordenada.y))

    player_image = pygame.transform.rotate(sprite, nave.angulo)
    player_rect = player_image.get_rect()
    player_rect.center = (nave.coordenada.x, nave.coordenada.y)
    screen.blit(player_image, player_rect)

    pygame.display.update()
