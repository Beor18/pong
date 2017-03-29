# importar modulos de pygame
# PONG, THE REVENGE OF THE DIEGO

import pygame, sys
from pygame.locals import *

ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho,alto))

fondo = pygame.image.load("imagenes/fondo1.jpg")
pelota = pygame.image.load("imagenes/pelota1.png")
paleta_jugador = pygame.image.load("imagenes/paleta.png")
paleta_ia = pygame.image.load("imagenes/paleta.png")

# bolax = 100
# bolay = 300
bolavelx = 20

#Definir Sprite Pelota

sprite_pelota = pygame.sprite.Sprite()
sprite_pelota.image = pelota 

#Toma el ancho y alto de la imagen
sprite_pelota.rect = pelota.get_rect()

# Velocidad Sprite
sprite_pelota.rect.x = 100
sprite_pelota.rect.y = 100

while True:
	
	#Salir
	for evento in pygame.event.get():
		if evento.type == QUIT:
			print "##############"
			print "#  Saliendo  #"
			print "##############"
			sys.exit()
	
	#Movimiento bolax
	# bolax += bolavelx
	
	#fondo
	pantalla.blit(fondo,(0,0))
	
	#Posicion Pelota
	# pantalla.blit(sprite_pelota.image, sprite_pelota.rect)
	sprite_pelota.rect.x = bolavelx
	
	
	#otros objetos
	pantalla.blit(paleta_jugador, (50,150))
	pantalla.blit(paleta_ia, (580,150))		
	pygame.display.update()
