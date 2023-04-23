import random

import pygame


pygame.init()

#Game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500
background = white
player = pygame.transform.scale(pygame.image.load('zues.png'), (90, 70))
fps = 60
font = pygame.font.font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False


# Game variables
player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], 
        [265, 150, 70, 10], [175, 40 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
score_last = 0
super_jumps = 2
jump_last = 0

# Create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Cloud Hopper')

# Check for collision with clouds
def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and jump == False and y_change > 0:
            j = True
    return j


# Update player y position every loop
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = .4
    if jump:
        y_change = jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos


# Handle movement of platforms as game progresses
def update_platforms(my_list, y_pos, change):
    global score
    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][i] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
            score += 1
    return my_list


running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))
    blocks = []
    score_text = font.render('High Score: ' + str(high_score), True, black, background)
    screen.blit(score_text, (280, 0))
    high_score_text = font.render('Score: ' + str(score), True, black, background)
    screen.blit(high_score_text, (320, 20))
