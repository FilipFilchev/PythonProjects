
#Tetris Game Finito!

import pygame
from copy import deepcopy
from random import choice, randrange

pygame.display.set_caption("Tetris Pygame")


class TetrisGame:
    def __init__(self):
        self.shapes_coordinates = [
            [(-1, 0), (-2, 0), (0, 0), (1, 0)],
            [(0, -1), (-1, -1), (-1, 0), (0, 0)],
            [(-1, 0), (-1, 1), (0, 0), (0, -1)],
            [(0, 0), (-1, 0), (0, 1), (-1, -1)],
            [(0, 0), (0, -1), (0, 1), (-1, -1)],
            [(0, 0), (0, -1), (0, 1), (1, -1)],
            [(0, 0), (0, -1), (0, 1), (-1, 0)]
        ]

        self.shapes = [[pygame.Rect(x + BOARD_WIDTH // 2, y + 1, 1, 1) for x, y in shape] for shape in self.shapes_coordinates]
        self.cell_rect = pygame.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_shape, self.next_shape = deepcopy(choice(self.shapes)), deepcopy(choice(self.shapes))
        self.current_color, self.next_color = self._random_color(), self._random_color()
        self.game_score = 0
        self.cleared_lines = 0
        self.speed_counter, self.drop_speed, self.drop_frequency = 0, 60, 2000

    @staticmethod
    def _random_color():
        #RGB
        return randrange(30, 256), randrange(30, 256), randrange(30, 256)

    def _is_within_boundaries(self, shape):
        for piece in shape:
            if piece.x < 0 or piece.x > BOARD_WIDTH - 1:
                return False
            elif piece.y > BOARD_HEIGHT - 1 or self.board[piece.y][piece.x]:
                return False
        return True

    def game_over(self):
        for piece in self.current_shape:
            if self.board[piece.y][piece.x]:
                print("Game Over!")
                pygame.quit()
                exit()

    def play(self):
        while True:
            self._process_inputs()
            self._update_state()
            self._render_graphics()
            pygame.display.flip()
            game_timer.tick(GAME_SPEED)

    def _process_inputs(self):
        horizontal_movement, is_rotation = 0, False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    horizontal_movement = -1
                elif event.key == pygame.K_RIGHT:
                    horizontal_movement = 1
                elif event.key == pygame.K_DOWN:
                    self.drop_frequency = 100
                elif event.key == pygame.K_UP:
                    is_rotation = True

        # Move shape horizontally
        last_shape = deepcopy(self.current_shape)
        for piece in self.current_shape:
            piece.x += horizontal_movement
        if not self._is_within_boundaries(self.current_shape):
            self.current_shape = last_shape

        # Move shape downwards based on speed
        self.speed_counter += self.drop_speed
        if self.speed_counter > self.drop_frequency:
            self.speed_counter = 0
            last_shape = deepcopy(self.current_shape)
            for piece in self.current_shape:
                piece.y += 1
            if not self._is_within_boundaries(self.current_shape):
                for piece in last_shape:
                    self.board[piece.y][piece.x] = self.current_color
                self.current_shape, self.current_color = self.next_shape, self.next_color
                self.next_shape, self.next_color = deepcopy(choice(self.shapes)), self._random_color()
                self.drop_frequency = 2000
                self.game_over()

        # Rotate shape
        if is_rotation:
            center_point = self.current_shape[0]
            last_shape = deepcopy(self.current_shape)
            for i, piece in enumerate(self.current_shape):
                x = piece.y - center_point.y
                y = piece.x - center_point.x
                piece.x = center_point.x - x
                piece.y = center_point.y + y
            if not self._is_within_boundaries(self.current_shape):
                self.current_shape = last_shape

    def _update_state(self):
        current_line = BOARD_HEIGHT - 1
        self.cleared_lines = 0
        for row in range(BOARD_HEIGHT - 1, -1, -1):
            is_full = all(self.board[row])
            if not is_full:
                self.board[current_line] = self.board[row]
                current_line -= 1
            else:
                self.drop_speed += 3
                self.cleared_lines += 1
                print("Line cleared!")

        points = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
        self.game_score += points[self.cleared_lines]

    def _render_graphics(self):
        screen.blit(background_image, (0, 0))
        screen.blit(board_surface, (20, 20))
        board_surface.blit(board_bg_image, (0, 0))
        for piece in self.current_shape:
            self.cell_rect.x = piece.x * TILE_SIZE
            self.cell_rect.y = piece.y * TILE_SIZE
            pygame.draw.rect(board_surface, self.current_color, self.cell_rect)
        for y, row in enumerate(self.board):
            for x, cell_color in enumerate(row):
                if cell_color:
                    self.cell_rect.x, self.cell_rect.y = x * TILE_SIZE, y * TILE_SIZE
                    pygame.draw.rect(board_surface, cell_color, self.cell_rect)
        for piece in self.next_shape:
            self.cell_rect.x = piece.x * TILE_SIZE + 380
            self.cell_rect.y = piece.y * TILE_SIZE + 185
            pygame.draw.rect(screen, self.next_color, self.cell_rect)
        screen.blit(tetris_label, (505, 15))
        screen.blit(score_label, (535, 780))
        screen.blit(score_font.render(str(self.game_score), True, pygame.Color('green')), (550, 840))


# Constants
TILE_SIZE = 40
BOARD_WIDTH, BOARD_HEIGHT = 10, 20
BOARD_RESOLUTION = BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE
SCREEN_RESOLUTION = 700, 900
GAME_SPEED = 60
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
board_surface = pygame.Surface(BOARD_RESOLUTION)
game_timer = pygame.time.Clock()

cells = [pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) for x in range(BOARD_WIDTH) for y in range(BOARD_HEIGHT)]
background_image = pygame.image.load('./img/tetris1.jpeg').convert()
board_bg_image = pygame.image.load('./img/tetris2.png').convert()
header_font = pygame.font.Font(None, 70)
score_font = pygame.font.Font(None, 50)
tetris_label = header_font.render('TETRIS', True, pygame.Color('red'))
score_label = score_font.render('score:', True, pygame.Color('blue'))

if __name__ == '__main__':
    game = TetrisGame()
    game.play()
