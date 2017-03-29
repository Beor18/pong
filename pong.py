# importar modulos de pygame
# PONG, THE REVENGE OF THE DIEGO

import pygame, sys
from pygame.locals import *

ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho,alto))

fondo = pygame.image.load("imagenes/fondo1.jpg")
paleta_jugador = pygame.image.load("imagenes/paleta.png")
paleta_ia = pygame.image.load("imagenes/paleta.png")

# bolax = 100
# bolay = 300

#Definir Sprite Pelota
pelota = pygame.image.load("imagenes/pelota1.png")
sprite_pelota = pygame.sprite.Sprite()
sprite_pelota.image = pelota 
sprite_pelota.rect = pelota.get_rect()
sprite_pelota.rect.x = 100
sprite_pelota.rect.y = 100

#Velocidad
bolavelx = 10
bolavely = 10

#Reloj
clock = pygame.time.Clock()
FPS = 60

while True:
	
	#Salir
	for evento in pygame.event.get():
		if evento.type == QUIT:
			print "##############"
			print "#  Saliendo  #"
			print "##############"
			sys.exit()
	
	#Movimiento bolax
	sprite_pelota.rect.x += bolavelx
	
	#fondo
	pantalla.blit(fondo,(0,0))
	
	#Posicion Pelota
	pantalla.blit(sprite_pelota.image, sprite_pelota.rect)
	
	if sprite_pelota.rect.x+ sprite_pelota.rect.width > ancho:
		bolavelx = bolavelx *-1
		
	if sprite_pelota.rect.x < 0:
		bolavelx = bolavelx *-1
		
		
	# sprite_pelota.rect.x = bolavelx
	print clock.tick(FPS)
	
	#otros objetos
	pantalla.blit(paleta_jugador, (50,150))
	pantalla.blit(paleta_ia, (580,150))		
	pygame.display.update()
