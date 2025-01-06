import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

# you can use the bold = True or/and italic = True for them
text_font = pygame.font.SysFont("Arial", 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


speed = 8
score = 1
textx = 300
texty = 255
gravity = 7
white = (0, 0, 0)
col = (255, 0, 0)
col2 = (100, 100, 100)
enemy_color = (0, 0, 255)
start_time = pygame.time.get_ticks()
player = pygame.Rect((textx, texty, 50, 50))
wall = pygame.Rect(0, 0, 50, 600)
wall2 = pygame.Rect(200, 300, 300, 50)
floor = pygame.Rect(0, 590, 800, 50)
wall3 = pygame.Rect(750, 0, 50, 600)
enemy = pygame.Rect(random.randint(50, 750), 0, 50, 50)
room = [wall, wall2, wall3, floor]
rects = [
    (player, col),
    (wall, enemy_color),
    (wall2, enemy_color),
    (floor, enemy_color),
    (wall3, enemy_color),
    (enemy, enemy_color)
    ]
run = True
while run:

    pygame.display.set_caption("Moover")

    clock = pygame.time.Clock()

    if player.colliderect(room):
        col = col2

    elif player.colliderect(floor):
        pass

    else:
        col = (255, 0, 0)
        texty += gravity
        player.move_ip(0, gravity)
    screen.fill((0, 200, 0))

    # x always comes first then y (x, y)
    # movement scripts
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if player.colliderect(wall):
            pass
        else:
            player.move_ip((speed - speed*2), 0)
            textx -= speed
    if key[pygame.K_d]:
        if player.colliderect(wall3):
            pass
        else:
            player.move_ip(speed, 0)
            textx += speed
    if key[pygame.K_w]:
        player.move_ip(0, (speed - speed*3) - (gravity - speed))
        texty -= speed + speed + (gravity - speed)
    if key[pygame.K_s]:
        if player.colliderect(floor) or player.colliderect(wall2):
            pass
        else:
            player.move_ip(0, 1)
            texty += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    elapsed_time = pygame.time.get_ticks() - start_time

    if elapsed_time >= 1000:  # 1000 milliseconds = 1 second
        score += 1
        start_time = pygame.time.get_ticks()

    for rect, color in rects:
        pygame.draw.rect(screen, color, rect)

# draw the text
    draw_text(" me", text_font, (0, 0, 0), textx, texty)
    draw_text("Hello Player, welcome to the in-progress-program", text_font, (0, 0, 0,), 150, 100)
    draw_text(f"Score: {score}", text_font, (0, 0, 0,), 100, 50)

    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
