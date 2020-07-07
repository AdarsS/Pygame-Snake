import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')
running = True
clock = pygame.time.Clock()
score = 0


def game_over():
    game_font = pygame.font.Font('freesansbold.ttf', 64)
    gamer_over1 = game_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(gamer_over1, (200, 250))

# To keep count of the score


def score_value():
    font = pygame.font.Font('freesansbold.ttf', 32)
    score_value1 = font.render("Score: " + str(score), True, (0, 225, 0))
    screen.blit(score_value1, (10, 10))


# Snake
x1 = 100  # Starting point of the snake
y1 = 400  # Starting point of the snake
snake_x = 0  # To record the change the snake in the x direction
snake_y = 0  # To record the change the snake in the y direction
snake_size = 17
snake_speed = 25
blue = (0, 0, 255)
snake_List = []
length_of_snake = 1

# Food
yellow = (255, 255, 0)
x2 = random.randint(20, 780)
y2 = random.randint(20, 580)


def snake(snake_list):
    for x3 in snake_list:
        pygame.draw.rect(screen, blue, [x3[0], x3[1], snake_size, snake_size])


def food(c, d):
    pygame.draw.rect(screen, yellow, [c, d, 10, 10])


# Snake with food collision
def is_collision(snake_x1, snake_y1, food_x1, food_y1):
    distance = math.sqrt((math.pow(snake_x1 - food_x1, 2)) + (math.pow(snake_y1 - food_y1, 2)))
    if distance < 15:
        return True
    else:
        return False


while running:
    screen.fill((0, 0, 0))  # Black background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                running = True
            if event.key == pygame.K_LEFT:
                snake_x = -10
                snake_y = 0
            if event.key == pygame.K_RIGHT:
                snake_x = 10
                snake_y = 0
            if event.key == pygame.K_UP:
                snake_y = -10
                snake_x = 0
            if event.key == pygame.K_DOWN:
                snake_y = 10
                snake_x = 0

    snake_head = [x1, y1]
    snake_List.append(snake_head)
    if len(snake_List) > length_of_snake:
        del snake_List[0]
    x1 += snake_x
    y1 += snake_y

    # Snake when it hits itself
    for x in snake_List[:-1]:
        if x == snake_head:
            game_over()
            x1 = 3000
            y1 = 3000

    # Snake when it goes out of the screen
    if x1 < 0 or x1 > 800 or y1 < 0 or y1 > 600:
        game_over()
        x1 = 3000
        x2 = 3000

    # If collision happens with food
    collision = is_collision(x1, y1, x2, y2)
    if collision:
        x2 = random.randint(20, 780)
        y2 = random.randint(20, 580)
        length_of_snake += 1
        score += 1

    snake(snake_List)
    food(x2, y2)
    score_value()
    pygame.display.update()
    clock.tick(snake_speed)
