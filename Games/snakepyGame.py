"""
WHY DOESNT WORKS?

"""


# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set up the display
# WIDTH, HEIGHT = 640, 480
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snake Game")

# # Colors
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# # Snake initial position and size
# snake_size = 20
# snake_x = 100
# snake_y = 100
# snake_speed = 10

# # Snake body
# snake_body = []
# snake_length = 1

# # Food position
# food_x = random.randint(0, WIDTH - snake_size)
# food_y = random.randint(0, HEIGHT - snake_size)

# # Direction
# direction_x = 0
# direction_y = 0

# # Game Over flag
# game_over = False

# # Score
# score = 0
# font = pygame.font.SysFont(None, 30)

# # Function to draw snake and food
# def draw_snake(snake_body):
#     for x, y in snake_body:
#         pygame.draw.rect(WIN, GREEN, (x, y, snake_size, snake_size))

# def draw_food(food_x, food_y):
#     pygame.draw.rect(WIN, RED, (food_x, food_y, snake_size, snake_size))

# def display_score(score):
#     score_text = font.render("Score: " + str(score), True, BLACK)
#     WIN.blit(score_text, (10, 10))

# # Game loop
# clock = pygame.time.Clock()

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 direction_x = -snake_size
#                 direction_y = 0
#             elif event.key == pygame.K_RIGHT:
#                 direction_x = snake_size
#                 direction_y = 0
#             elif event.key == pygame.K_UP:
#                 direction_y = -snake_size
#                 direction_x = 0
#             elif event.key == pygame.K_DOWN:
#                 direction_y = snake_size
#                 direction_x = 0

#     snake_x += direction_x
#     snake_y += direction_y

#     # Check if snake eats food
#     if snake_x == food_x and snake_y == food_y:
#         food_x = random.randint(0, WIDTH - snake_size)
#         food_y = random.randint(0, HEIGHT - snake_size)
#         snake_length += 1
#         score += 10

#     # Check if snake hits itself or the boundary
#     if [snake_x, snake_y] in snake_body[:-1] or snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
#         game_over = True

#     snake_head = []
#     snake_head.append(snake_x)
#     snake_head.append(snake_y)
#     snake_body.append(snake_head)

#     if len(snake_body) > snake_length:
#         del snake_body[0]

#     WIN.fill(BLACK)
#     draw_snake(snake_body)
#     draw_food(food_x, food_y)
#     display_score(score)

#     pygame.display.update()

#     clock.tick(snake_speed)

# # Quit the game
# pygame.quit()


import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by ChatGPT')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    rendered_msg = font_style.render(msg, True, color)
    dis.blit(rendered_msg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
