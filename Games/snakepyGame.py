import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)
RED = (213, 50, 80)

# Create clock object
CLOCK = pygame.time.Clock()

# Define screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Python Snake Game - NostalgiaGame')

# Define font style
FONT_STYLE = pygame.font.SysFont(None, 30)


# Define snake size and speed
SNAKE_SIZE = 20  
SNAKE_SPEED = 15

# Function to display a message on the screen
def display_message(msg, color):
    rendered_msg = FONT_STYLE.render(msg, True, color)
    SCREEN.blit(rendered_msg, [SCREEN_WIDTH/5, SCREEN_HEIGHT/2]) 
    #SCREEN_WIDTH - SNAKE_SIZE

# Function to draw the snake on the screen
def draw_snake(SNAKE_SIZE, snake_positions):
    for pos in snake_positions:
        pygame.draw.rect(SCREEN, GREEN, [pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE])  # Snake in Green

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initialize snake position
    snake_x = SCREEN_WIDTH/2
    snake_y = SCREEN_HEIGHT/2

    # Initialize snake direction
    snake_x_change = 0
    snake_y_change = 0

    # Initialize snake positions list
    snake_positions = []
    snake_length = 1

    # Initialize food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE) / 20.0) * 20.0

    # Game loop
    while not game_over:

        # Game over loop
        while game_close == True:
            SCREEN.fill(BLUE)
            display_message("You Lost :( Press Q-Quit or C-Play Again", RED)
           

            pygame.display.update()

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake_x_change = SNAKE_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_LEFT:
                    snake_x_change = -SNAKE_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -SNAKE_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = SNAKE_SIZE
                    snake_x_change = 0

        # Check if snake hits the boundary
        if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
            game_close = True

        # Update snake position
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Fill the screen
        SCREEN.fill(BLACK)

        # Draw the food
        pygame.draw.rect(SCREEN, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])  # Food in RED

        # Update snake positions
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_positions.append(snake_head)
        if len(snake_positions) > snake_length:
            del snake_positions[0]

        # Check if snake hits itself
        for pos in snake_positions[:-1]:
            if pos == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(SNAKE_SIZE, snake_positions)
        pygame.display.update()

        # Check if snake eats the food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE) / 20.0) * 20.0
            snake_length += 1

        #CHeck
        print(f"Snake Position: {snake_x}, {snake_y} | Food Position: {food_x}, {food_y}")

        # Cap the frame rate
        CLOCK.tick(SNAKE_SPEED)

    # Quit the game
    pygame.quit()

# Start the game
game_loop()
