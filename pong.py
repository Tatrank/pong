import pygame

time = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 600))
Running = True
pong1 = pygame.transform.scale(pygame.image.load("pong2.png").convert(), (15, 72))
pong2 = pygame.transform.scale(pygame.image.load("pong2.png").convert(), (15, 72))
pong1_rect = pong1.get_rect(center = (30, 300))
pong2_rect = pong2.get_rect(center = (970, 300))
ball = pygame.transform.scale(pygame.image.load("pong2.png").convert(), (20, 20))
ball_rect = ball.get_rect(center = (500, 300))
velocity_x = 6
velocity_y = 0


def render():
    screen.fill("black")
    screen.blit(pong1, pong1_rect)
    screen.blit(pong2, pong2_rect)
    screen.blit(ball, ball_rect)
    pygame.display.update()

def movement_pong1():
    if keys[pygame.K_w] and pong1_rect.top >= 10:
        pong1_rect.y -= 4

    if keys[pygame.K_s] and pong1_rect.bottom <= 590:
        pong1_rect.y += 4

def movement_pong2():
    if keys[pygame.K_UP] and pong2_rect.top >= 10:
        pong2_rect.y -= 4

    if keys[pygame.K_DOWN] and pong2_rect.bottom <= 590:
        pong2_rect.y += 4




while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    keys = pygame.key.get_pressed()
    render()


    if pong1_rect.colliderect(ball_rect):
        velocity_x = 6
        if ball_rect.centery < (pong1_rect.centery) and ball_rect.centery > (pong1_rect.top - 10):
            velocity_y = -1
        if ball_rect.centery > (pong1_rect.centery) and ball_rect.centery < (pong1_rect.bottom + 10):
            velocity_y = 1
        print(pong1_rect.centery, pong1_rect.top, ball_rect.centery)
    if pong2_rect.colliderect(ball_rect):
        velocity_x = -6
        if ball_rect.centery < (pong2_rect.centery) and ball_rect.centery > (pong2_rect.top +10):
            velocity_y = -1
        if ball_rect.centery > (pong2_rect.centery) and ball_rect.centery < (pong2_rect.bottom - 10):
            velocity_y = 1
        print(velocity_y, velocity_x)

    if ball_rect.top == 0 or ball_rect.bottom == 600:
        velocity_y = -velocity_y

    if ball_rect.left <= 0 or ball_rect.right >= 1000:
        ball_rect.center = (500, 300)
        velocity_y = 0
    ball_rect.x += velocity_x
    ball_rect.y += velocity_y


    movement_pong1()
    movement_pong2()
    time.tick(60)

pygame.quit()
