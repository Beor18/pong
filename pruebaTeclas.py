import pygame
pygame.init()
screen = pygame.display.set_mode((680, 460))
clock = pygame.time.Clock()



paddle = pygame.Rect((0, 0, 20, 80))

while True:

    if pygame.event.get(pygame.QUIT): 
		break
    pygame.event.pump()

 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: 
		paddle.move_ip(0, -7)
    if keys[pygame.K_DOWN]: 
		paddle.move_ip(0, 7)
    if keys[pygame.K_RIGHT]: 
		paddle.move_ip(7, 0)
    if keys[pygame.K_LEFT]: 
		paddle.move_ip(-7, 0)


    paddle.clamp_ip(screen.get_rect())

    screen.fill((0,0,0))    
    pygame.draw.rect(screen, (255,255,255), paddle)
    pygame.display.flip()

    clock.tick(60)
