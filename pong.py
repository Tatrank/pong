import pygame

time = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 600))
Running = True
pong1 = pygame.transform.scale(pygame.image.load("pong2.png").convert(), (15, 72))
pong2 = pygame.transform.scale(pygame.image.load("pong2.png").convert(), (15, 72))
pong1_rect = pong1.get_rect(center=(30, 300))
pong2_rect = pong2.get_rect(center=(970, 300))
ball = pygame.transform.scale(pygame.image.load("pong2.png").convert(), (20, 20))
ball_rect = ball.get_rect(center=(500, 300))
velocity_x = 6
velocity_y = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score1 = 0
score2 = 0
text = font.render(f"{score1}:{score2}", True, "white")


def render():
    screen.fill("black")
    screen.blit(pong1, pong1_rect)
    screen.blit(pong2, pong2_rect)
    screen.blit(ball, ball_rect)
    screen.blit(text, (50, 40))
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


def reset():
    ball_rect.center = (500, 300)
    pong1_rect.center = (30, 300)
    pong2_rect.center = (970, 300)


while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    keys = pygame.key.get_pressed()
    render()

    if pong1_rect.colliderect(ball_rect):
        velocity_x = 6
        if pong1_rect.centery > ball_rect.centery > (pong1_rect.top - 10):
            velocity_y = (-((-pong1_rect.top + ball_rect.centery) / 100) - 1) * 4
        elif pong1_rect.centery < ball_rect.centery < (pong1_rect.bottom + 10):
            velocity_y = (((-pong1_rect.top + ball_rect.centery) / 100) + 1) * 4

    if pong2_rect.colliderect(ball_rect):
        velocity_x = -6
        if pong2_rect.centery > ball_rect.centery > (pong2_rect.top + 10):
            velocity_y = -((-pong2_rect.top + ball_rect.centery) / 100) * 4
        elif pong2_rect.centery < ball_rect.centery < (pong2_rect.bottom - 10):
            velocity_y = -((-pong2_rect.top + ball_rect.centery) / 100) * 4

    if ball_rect.top <= 0 or ball_rect.bottom >= 600:
        velocity_y = -velocity_y

    if ball_rect.left <= 0 or ball_rect.right >= 1000:
        reset()
        velocity_y = 0
        if velocity_x > 0:
            score1 += 1
            text = font.render(f"{score1}:{score2}", True, "white")
        if velocity_x < 0:
            score2 += 1
            text = font.render(f"{score1}:{score2}", True, "white")

    ball_rect.x += velocity_x
    ball_rect.y += velocity_y

    movement_pong1()
    movement_pong2()
    time.tick(60)

pygame.quit()
