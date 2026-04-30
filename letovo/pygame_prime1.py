import pygame
 
SIZE = W, H = 800, 600
WIHE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60 

 
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()

screen.fill(WHITE)
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    #основной код
    pygame.draw.circle(screen, RED, (100, 100), 50)
 
    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()
 
