"""TICTACTOE GAME recreation In PYGAME by Vision"""


import pygame
import math

pygame.init()
clock = pygame.time.Clock()


# Screen setup
SCREEN_SIZE = 400
DIVISIONS = 3
display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("TicTacToe Pygame by |Vision| ")

# Define colors
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (200, 200, 200)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (220, 0, 0)

# Load and scale X and O images
IMG_X = pygame.transform.scale(pygame.image.load("images/x1.png"), (90, 90))
IMG_O = pygame.transform.scale(pygame.image.load("images/o.png"), (90, 90))

# Load Dark mode button image
IMG_DARK_MODE_BUTTON = pygame.transform.scale(pygame.image.load("images/toggle_mode.png"), (20, 20))

# Dark mode button setup
dark_mode = False
dark_mode_button = pygame.Rect(10, 10, 20, 20)

# Define font for end game message
FONT_END = pygame.font.SysFont('calibri', 50)

# Draw TicTacToe grid on the game screen
def grid():
    gap = SCREEN_SIZE // DIVISIONS
    for i in range(DIVISIONS):
        pos = i * gap
        pygame.draw.line(display, COLOR_GRAY, (pos, 0), (pos, SCREEN_SIZE), 5)
        pygame.draw.line(display, COLOR_GRAY, (0, pos), (SCREEN_SIZE, pos), 5)

# Initialize the game state grid with empty cells
def grid_initialize():

    print("Initializing game state...")

    game_state = [
        [None, None, None],
        [None, None, None], 
        [None, None, None]]

    offset = SCREEN_SIZE // DIVISIONS // 2
    game_state = [[(offset * (2*j+1), offset * (2*i+1), '', True) for j in range(DIVISIONS)] for i in range(DIVISIONS)]
    return game_state


""" 
For generating evenly-spaced grid:

The factor 2 is there to ensure that there is a gap between each cell, effectively creating "grid lines". If we just used j or i, the cells would be directly adjacent to each other, without any space in between.
The +1 is used to ensure that the first cell starts at the correct offset. Without this, the first cell would start at the position (0,0), right at the top-left corner of the game window. By adding 1, we ensure that there is a gap equivalent to one cell size around the edge of the board.
Together, 2*j+1 and 2*i+1 ensure that the cells are correctly positioned in a grid with spaces in between and around the edge.

Suppose offset is 10, and you have a 3x3 grid (DIVISIONS is 3). The x and y positions of the cells would be calculated as follows:

j (or i)	2*j+1	offset*(2*j+1)
0	1	10
1	3	30
2	5	50
"""


# Render the game screen with updated game state
def game_render():
    if dark_mode:
        display.fill(COLOR_BLACK)
        text_color = COLOR_WHITE
    else:
        display.fill(COLOR_WHITE)
        text_color = COLOR_BLACK
    
    grid()
    for img in image_list:
        x, y, IMAGE = img
        display.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    
    # Add the dark mode button
    display.blit(IMG_DARK_MODE_BUTTON, (dark_mode_button.x, dark_mode_button.y))
    
    pygame.display.update()


# Handle the event when a player clicks on a cell
def click_handler(game_state):

    global turn_x, turn_o, image_list
    m_x, m_y = pygame.mouse.get_pos()

    for i in range(len(game_state)):
        for j in range(len(game_state[i])):
            cell_x, cell_y, cell_char, playable = game_state[i][j]
            #dist mouse and the centre of the square
            distance = math.sqrt((cell_x - m_x)**2 + (cell_y - m_y)**2)
            if distance < SCREEN_SIZE // DIVISIONS // 2 and playable:
                if turn_x:
                    print("Player X placed in cell", i, j)
                    image_list.append((cell_x, cell_y, IMG_X))
                    turn_x, turn_o = False, True
                    game_state[i][j] = (cell_x, cell_y, 'x', False)
                elif turn_o:
                    print("Player O placed in cell", i, j)
                    image_list.append((cell_x, cell_y, IMG_O))
                    turn_x, turn_o = True, False
                    game_state[i][j] = (cell_x, cell_y, 'o', False)

# Check if the game has been won by any player
def check_win(game_state):

    # Check rows, columns, and diagonals for a winning line
    #rows
    for row in range(len(game_state)):
        if game_state[row][0][2] == game_state[row][1][2] == game_state[row][2][2] != "":
            draw_winning_line((0, row), (2, row))
            game_end_message(game_state[row][0][2].upper() + " wins!")
            return True
    #cols
    for col in range(len(game_state)):
        if game_state[0][col][2] == game_state[1][col][2] == game_state[2][col][2] != "":
            draw_winning_line((col, 0), (col, 2))
            game_end_message(game_state[0][col][2].upper() + " wins!")
            return True
    #main diag
    if game_state[0][0][2] == game_state[1][1][2] == game_state[2][2][2] != "":
        draw_winning_line((0, 0), (2, 2))
        game_end_message(game_state[0][0][2].upper() + " wins!")
        return True
    #reverse diag
    if game_state[0][2][2] == game_state[1][1][2] == game_state[2][0][2] != "":
        draw_winning_line((2, 0), (0, 2))
        game_end_message(game_state[0][2][2].upper() + " wins!")
        return True
    return False

def draw_winning_line(start, end):
    start_x, start_y = start
    end_x, end_y = end

    # Translate grid coordinates to pixel coordinates
    pixel_start_x = (start_x * SCREEN_SIZE // DIVISIONS) + (SCREEN_SIZE // DIVISIONS // 2)
    pixel_start_y = (start_y * SCREEN_SIZE // DIVISIONS) + (SCREEN_SIZE // DIVISIONS // 2)

    pixel_end_x = (end_x * SCREEN_SIZE // DIVISIONS) + (SCREEN_SIZE // DIVISIONS // 2)
    pixel_end_y = (end_y * SCREEN_SIZE // DIVISIONS) + (SCREEN_SIZE // DIVISIONS // 2)

    pygame.draw.line(display, COLOR_RED, (pixel_start_x, pixel_start_y), (pixel_end_x, pixel_end_y), 10)


# Check if game has reached a draw state
def check_draw(game_state):

    if all(game_state[i][j][2] != "" for j in range(len(game_state)) for i in range(len(game_state))):
        game_end_message("Game drawn!")
        return True
    return False

# Display game over message
def game_end_message(message):
    #wait
    pygame.time.delay(500)
    # Render the text first to get its dimensions
    end_text = FONT_END.render(message, 1, COLOR_BLACK)
    # Define padding for the rectangle around the text
    padding = 10  
    
    #rectangle dimensions
    rect_x = (SCREEN_SIZE - end_text.get_width()) // 2 - padding
    rect_y = (SCREEN_SIZE - end_text.get_height()) // 2 - padding
    rect_width = end_text.get_width() + 2 * padding
    rect_height = end_text.get_height() + 2 * padding
    
    # Draw the rectangle
    background_color = (255, 255, 153)  
    pygame.draw.rect(display, background_color, (rect_x, rect_y, rect_width, rect_height))
    
    # Blit the text onto the rectangle
    display.blit(end_text, ((SCREEN_SIZE - end_text.get_width()) // 2, (SCREEN_SIZE - end_text.get_height()) // 2))
    #update screen
    pygame.display.update()
    #wait before reboot
    pygame.time.delay(3000)



# Main loop + a check for the dark_mode button
def game_loop():

    global turn_x, turn_o, image_list
    image_list = []
    running = True
    turn_x, turn_o = True, False
    game_state = grid_initialize()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                
                # Check if the dark_mode button was clicked
                if dark_mode_button.collidepoint((m_x, m_y)):
                    global dark_mode
                    dark_mode = not dark_mode  # toggle the mode
                else:
                    click_handler(game_state)
        game_render()
        if check_win(game_state) or check_draw(game_state):
            try: display.fill(COLOR_WHITE)
            except: raise ValueError 
            text_color = COLOR_WHITE
            game_end_message("Game Reboot")
            running = False
            print("Game over!, Rebooting..")
            
        clock.tick(60)
#execute!
while True:
    if __name__ == '__main__':
        game_loop()
        
        
