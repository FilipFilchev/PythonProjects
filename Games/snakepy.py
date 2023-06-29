import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake initial position and size
snake_size = 20
snake_x = 100
snake_y = 100
snake_speed = 10

# Snake body
snake_body = []
snake_length = 1

# Food position
food_x = random.randint(0, WIDTH - snake_size)
food_y = random.randint(0, HEIGHT - snake_size)

# Direction
direction_x = 0
direction_y = 0

# Game Over flag
game_over = False

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Function to draw snake and food
def draw_snake(snake_body):
    for x, y in snake_body:
        pygame.draw.rect(WIN, GREEN, (x, y, snake_size, snake_size))

def draw_food(food_x, food_y):
    pygame.draw.rect(WIN, RED, (food_x, food_y, snake_size, snake_size))

def display_score(score):
    score_text = font.render("Score: " + str(score), True, BLACK)
    WIN.blit(score_text, (10, 10))

# Game loop
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction_x = -snake_size
                direction_y = 0
            elif event.key == pygame.K_RIGHT:
                direction_x = snake_size
                direction_y = 0
            elif event.key == pygame.K_UP:
                direction_y = -snake_size
                direction_x = 0
            elif event.key == pygame.K_DOWN:
                direction_y = snake_size
                direction_x = 0

    snake_x += direction_x
    snake_y += direction_y

    # Check if snake eats food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, WIDTH - snake_size)
        food_y = random.randint(0, HEIGHT - snake_size)
        snake_length += 1
        score += 10

    # Check if snake hits itself or the boundary
    if [snake_x, snake_y] in snake_body[:-1] or snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    WIN.fill(BLACK)
    draw_snake(snake_body)
    draw_food(food_x, food_y)
    display_score(score)

    pygame.display.update()

    clock.tick(snake_speed)

# Quit the game
pygame.quit()
