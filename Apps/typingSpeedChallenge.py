#libs
import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BG_COLOR = (10, 10, 10)
WORD_COLOR = (255, 255, 255)
OUTPUT_COLOR = (255, 0, 0)
FONT_STYLE = 'arial'
FONT_SIZE = 40
WORDS_LIST = ["world","Filip", "hello", "typing", "speed", "game", "python", "pygame"]

# Set up display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Speed Typing Challenge")

# Set up fonts
main_font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
output_font = pygame.font.SysFont(FONT_STYLE, 20)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# WPM=(Number of Characters Typed/5)/(Elapsed Time/60). 
# The factor of 5 in the numerator is used because one word is typically considered to be 5 characters long in typing speed tests.

def main():
    game_over = False
    clock = pygame.time.Clock()
    target_word = random.choice(WORDS_LIST)
    typed_word = ''
    begin_time = None
    output_text = ""

    #handle game events
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                #Key_...key
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_BACKSPACE:
                    typed_word = typed_word[:-1]
                elif event.key == pygame.K_RETURN:
                    if typed_word == target_word:
                        elapsed_time = time.time() - begin_time
                        wpm = int((len(target_word) / 5) / (elapsed_time / 60))
                        output_text = f'Words per minute: {wpm}'
                        target_word = random.choice(WORDS_LIST)
                        typed_word = ''
                        begin_time = time.time()
                    else:
                        output_text = 'Incorrect word. Please try again!'
                        typed_word = ''
                else:
                    typed_word += event.unicode
        #clear scr
        window.fill(BG_COLOR)

        draw_text(target_word, main_font, WORD_COLOR, window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100)
        draw_text(typed_word, main_font, WORD_COLOR, window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        draw_text(output_text, output_font, OUTPUT_COLOR, window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)
        
        # Update screen
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)
        #start calculating time
        if begin_time is None:
            begin_time = time.time()
#run the game loop
main()
pygame.quit()