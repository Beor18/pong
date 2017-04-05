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
sprite_pelota.rect.x = 200
sprite_pelota.rect.y = 200

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
sprite_paleta_jugador.centery = sprite_paleta_jugador.rect.height/2


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

paletaJ_vely = 15
paletaI_vely = 15
while True:
	
	#Salir
	if pygame.event.get(pygame.QUIT):
		break
			
	for evento in pygame.event.get():
		teclas = pygame.key.get_pressed()
			
		if pygame.event.get(pygame.QUIT): 
			break
		# pygame.event.pump()
	
		
		if evento.type == pygame.KEYDOWN:
			if teclas[K_DOWN]:
				sprite_paleta_jugador.rect.y += paletaJ_vely
			if teclas[K_UP]:
				sprite_paleta_jugador.rect.y -= paletaJ_vely
	
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
	
	# sprite_paleta_jugador.rect.centery = sprite_pelota.rect.centery
	
	# Limites de la pantalla.
	if sprite_paleta_jugador.rect.y + sprite_paleta_jugador.rect.height > alto:
		sprite_paleta_jugador.rect.y = sprite_paleta_jugador.rect.height
	elif sprite_paleta_jugador.rect.y < 0:
		sprite_paleta_jugador.rect.y = 0
	elif sprite_paleta_jugador.rect.y + sprite_paleta_jugador.rect.height > alto:
		sprite_paleta_ia.rect.y = sprite_paleta_jugador.rect.height
	elif sprite_paleta_ia.rect.y < 0:
		sprite_paleta_ia.rect.y = 0
	
	#Colision
	# Colision de Sprites.
	if sprite_pelota.rect.colliderect(sprite_paleta_jugador):
		bolavelx = bolavelx*-1
		print "COLISION JUGADOR"
	if sprite_pelota.rect.colliderect(sprite_paleta_ia):
		bolavelx = bolavelx*-1
		print "COLISION IA"
		
	#Cuadros por segundos
	print "FPS: ", clock.tick(FPS)
	
		
		
	pygame.display.update()
