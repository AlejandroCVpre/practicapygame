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
nave = player()

# Carga de fondo e imagenes
screen = pygame.display.set_mode((1024, 768), 0, 32)  # Tamaño de la ventana
sprite = pygame.image.load(nave.sprite_filename).convert_alpha()
background = pygame.image.load('imagenes/meme.jpg').convert()

# Main loop, llama las funciones que calculan las coordenadas de los elementos y los dibuja en pantalla. Las coordenadas
# de los elementos se guardan en el objeto, se llama con "objeto.coordenada.x o y"

balas = []
while True:
    screen.blit(background, (0, 0))
    nave.update(time_passed_seconds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            velocidad_bala = nave.velocidad_relativa_raton(nave.bullet_speed)
            balas.append(proyectil(nave.coordenada, velocidad_bala))

    for b in balas:
        b.update(time_passed_seconds)
        screen.blit(b.image, (b.coordenada.x, b.coordenada.y))

    player_image = pygame.transform.rotate(sprite, nave.angulo)
    player_rect = player_image.get_rect()
    player_rect.center = (nave.coordenada.x, nave.coordenada.y)
    screen.blit(player_image, player_rect)

    pygame.display.update()
