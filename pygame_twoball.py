import pygame
 
SIZE = WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WHITE = (0, 255, 0)
FPS = 60
 
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
 
running = True
ball_x, ball_y = 200, 200
ball_x2, ball_y2 = 200, 200
dx, dy = 5, 5
radius = 20
x, y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx = -5
        if event.key == pygame.K_RIGHT:
            dx = 5
        if event.key == pygame.K_DOWN:
            dy = 5
        if event.key == pygame.K_UP:
            dy = -5
 
    if ball_x > WIDTH:
        dx = -5
    if ball_x < 0:
        dx = 5
 
    if ball_y > HEIGHT:
        dy = -5
    if ball_y < 50:
        dy = 5
 
    screen.fill(WHITE)
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
       x, dx = dx, x
       y, dy = dy, y
 
    ball_x += dx
    ball_y += dy
    ball_x2 -= dx
    ball_y2 -= dy
    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)
    pygame.draw.circle(screen, GREEN, (ball_x2, ball_y2), 10)
    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()
