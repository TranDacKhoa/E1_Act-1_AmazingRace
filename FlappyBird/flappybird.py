import pygame
from random import randint

WIDTH = 400
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy Bird')

running = True

GREEN = (0,250,0)
BLUE = (0,0,255)
RED = (255, 0 , 0)
BLACK = (0,0,0)
YELLOW = (255,255,0)

clock = pygame.time.Clock()


TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35

bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont('sans' ,20)

tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False

backround_image = pygame.image.load("bg.png")
bird_image = pygame.image.load("redbird-midflap.png")
bird_image = pygame.transform.scale(bird_image,(BIRD_WIDTH, BIRD_HEIGHT))

while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(backround_image, (-100,0))

    #Vẽ ống
    tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x,0,TUBE_WIDTH,tube1_height))
    tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x,0,TUBE_WIDTH,tube2_height))
    tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x,0,TUBE_WIDTH,tube3_height))

    #Vẽ ống ngược lại
    tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
    tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
    tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))

    #Di chuyển ống sang trái
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    #Vẽ mặt đất
    sand_rect = pygame.draw.rect(screen,YELLOW, (0,550,400,50))

    #Vẽ bầu trời
    sky_rect = pygame.draw.rect(screen, BLUE,(0,0,400,5))

    #Vẽ chim
    bird_rect = screen.blit(bird_image,(BIRD_X, bird_y))

    #Chim rơi xuống
    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAVITY

    #Tạo ống mới
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_pass = False
        tube2_height = randint(100,400)
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False

    score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt, (5,5))

    #update score

    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score += 1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
        score += 1
        tube2_pass = True
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
        score += 1
        tube3_pass = True

    #Kiểm tra va chạm
    for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect,sky_rect]:
        if bird_rect.colliderect(tube):
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            game_over_txt = font.render("GAME OVER! Score: " + str(score), True, BLACK)
            screen.blit(game_over_txt, (150,300))
            press_space_txt = font.render("Press SPACE to Continue" , True, BLACK)
            screen.blit(press_space_txt, (150,350) )
            pausing = True
           

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:               
                #reset
                if pausing:
                    bird_y = 400
                    TUBE_VELOCITY = 3
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    score = 0
                    pausing = False
                

                bird_drop_velocity = 0
                bird_drop_velocity -= 10

    pygame.display.flip()

pygame.quit()