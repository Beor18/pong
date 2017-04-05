# importar modulos de pygame
# PONG, THE REVENGE OF THE DIEGO

import pygame, sys
from pygame.locals import *

ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho,alto))

fondo = pygame.image.load("imagenes/fondo1.jpg")


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

#Definir Sprite Paleta Jugador
paleta_jugador = pygame.image.load("imagenes/paleta.png")
sprite_paleta_jugador = pygame.sprite.Sprite()
sprite_paleta_jugador.image = paleta_jugador 
sprite_paleta_jugador.rect = paleta_jugador.get_rect()
sprite_paleta_jugador.rect.x = 50
sprite_paleta_jugador.rect.y = 150


#Definir Sprite Paleta IA
paleta_ia = pygame.image.load("imagenes/paleta.png")
sprite_paleta_ia = pygame.sprite.Sprite()
sprite_paleta_ia.image = paleta_ia 
sprite_paleta_ia.rect = paleta_ia.get_rect()
sprite_paleta_ia.rect.x = 580
sprite_paleta_ia.rect.y = 150


#Cuadros Por segundo
clock = pygame.time.Clock()
FPS = 60

while True:
	
	#Teclado
	for evento in pygame.event.get():
		if evento.type == QUIT:
			sys.exit()
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_DOWN:
				sprite_paleta_jugador.rect.y += bolavely
				print "Moviendo Abajo"
		if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_UP:
				sprite_paleta_jugador.rect.y -= bolavely
				print "Moviendo Arriba"	
	
	#Salir
	for evento in pygame.event.get():
		if evento.type == QUIT:
			print "##############"
			print "#  Saliendo  #"
			print "##############"
			sys.exit()
	
	#Movimiento bolax
	sprite_pelota.rect.x += bolavelx
	sprite_pelota.rect.y += bolavely
	
	#fondo
	pantalla.blit(fondo,(0,0))
	
	#Posicion Pelota
	pantalla.blit(sprite_pelota.image, sprite_pelota.rect)
	
	if sprite_pelota.rect.x+ sprite_pelota.rect.width > ancho:
		bolavelx = bolavelx *-1
		
	elif sprite_pelota.rect.x < 0:
		bolavelx = bolavelx *-1
		
	elif sprite_pelota.rect.y+ sprite_pelota.rect.height > alto:
		bolavely = bolavely *-1
	
	elif sprite_pelota.rect.y < 0:
		bolavely = bolavely *-1
	
	#Posicion Paleta Jugador
	pantalla.blit(sprite_paleta_jugador.image, sprite_paleta_jugador.rect)
	
	#Posicion Paleta IA
	pantalla.blit(sprite_paleta_ia.image, sprite_paleta_ia.rect)
	
	
	# Limites de la pantalla.
	if sprite_paleta_jugador.rect.y + sprite_paleta_jugador.rect.height > alto:
		sprite_paleta_jugador.rect.y = sprite_paleta_jugador1.rect.height
	elif sprite_paleta_jugador.rect.y < 0:
		sprite_paleta_jugador.rect.y = 0
	elif sprite_paleta_jugador.rect.y + sprite_paleta_jugador.rect.height > alto:
		sprite_paleta_ia.rect.y = sprite_paleta_jugador.rect.height
	elif sprite_paleta_ia.rect.y < 0:
		sprite_paleta_ia.rect.y = 0
	
	#Colision
	if pygame.sprite.collide_rect(sprite_pelota, sprite_paleta_jugador):
		bolavely = bolavely*-1
		print "Colision"
		
	elif pygame.sprite.collide_rect(sprite_pelota, sprite_paleta_ia):
		bolavely = bolavely*-1
		print "Colision 2"
		
	#Cuadros por segundos
	print "FPS: ", clock.tick(FPS)
	
		
		
	pygame.display.update()
