import pygame as pg
import numpy as np
import pygame.camera


class Matrix:
    def __init__(self, app, font_size=8):
        self.app = app
        self.FONT_SIZE = font_size
        self.SIZE = self.ROWS, self.COLS = app.HEIGHT // font_size, app.WIDTH // font_size
        self.katakana = np.array([chr(int('0x30a0', 16) + i) for i in range(96)] + ['' for i in range(10)])
        self.font = pg.font.Font('font/ms mincho.ttf', font_size, bold=True)

        self.matrix = np.random.choice(self.katakana, self.SIZE)
        self.char_intervals = np.random.randint(25, 50, size=self.SIZE)
        self.cols_speed = np.random.randint(1, 500, size=self.SIZE)
        self.prerendered_chars = self.get_prerendered_chars()

        # self.image = self.get_image('img/k1.png')

    def get_frame(self):
        image = app.cam.get_image()
        image = pg.transform.scale(image, self.app.RES)
        pixel_array = pg.pixelarray.PixelArray(image)
        return pixel_array

    def get_image(self, path_to_file):
        image = pg.image.load(path_to_file)
        image = pg.transform.scale(image, self.app.RES)
        pixel_array = pg.pixelarray.PixelArray(image)
        return pixel_array

    def get_prerendered_chars(self):
        char_colors = [(0, green, 0) for green in range(256)]
        prerendered_chars = {}
        for char in self.katakana:
            prerendered_char = {(char, color): self.font.render(char, True, color) for color in char_colors}
            prerendered_chars.update(prerendered_char)
        return prerendered_chars

    def run(self):
        frames = pg.time.get_ticks()
        self.change_chars(frames)
        self.shift_column(frames)
        self.draw()

    def shift_column(self, frames):
        num_cols = np.argwhere(frames % self.cols_speed == 0)
        num_cols = num_cols[:, 1]
        num_cols = np.unique(num_cols)
        self.matrix[:, num_cols] = np.roll(self.matrix[:, num_cols], shift=1, axis=0)

    def change_chars(self, frames):
        mask = np.argwhere(frames % self.char_intervals == 0)
        new_chars = np.random.choice(self.katakana, mask.shape[0])
        self.matrix[mask[:, 0], mask[:, 1]] = new_chars

    def draw(self):
        self.image = self.get_frame()
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                if char:
                    pos = x * self.FONT_SIZE, y * self.FONT_SIZE
                    _, red, green, blue = pg.Color(self.image[pos])
                    if red and green and blue:
                        color = (red + green + blue) // 3
                        color = 220 if 160 < color < 220 else color
                        char = self.prerendered_chars[(char, (0, color, 0))]
                        char.set_alpha(color + 60)
                        self.app.surface.blit(char, pos)


class MatrixVision:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 960, 720
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES)
        self.clock = pg.time.Clock()
        self.matrix = Matrix(self)

        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.cam.start()

    def draw(self):
        self.surface.fill(pg.Color('black'))
        self.matrix.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    app = MatrixVision()
    app.run()


"""

import pygame as pg
import numpy as np
import pygame.camera


class MatrixEffect:
    def __init__(self, vision_app, font_size=8):
        self.vision_app = vision_app
        self.FONT_SIZE = font_size
        self.DIMENSIONS = self.ROWS, self.COLS = vision_app.HEIGHT // font_size, vision_app.WIDTH // font_size
        self.katakana_symbols = np.array([chr(int('0x30a0', 16) + i) for i in range(96)] + ['' for i in range(10)])
        self.font = pg.font.Font('font/ms mincho.ttf', font_size, bold=True)

        # Initialize matrix with random katakana symbols
        self.matrix = np.random.choice(self.katakana_symbols, self.DIMENSIONS)
        self.char_intervals = np.random.randint(25, 50, size=self.DIMENSIONS)
        self.column_speeds = np.random.randint(1, 500, size=self.DIMENSIONS)
        self.rendered_chars_cache = self.cache_rendered_chars()

    def capture_camera_frame(self):
        frame = self.vision_app.camera.get_image()
        scaled_frame = pg.transform.scale(frame, self.vision_app.RESOLUTION)
        return pg.pixelarray.PixelArray(scaled_frame)

    def cache_rendered_chars(self):
        colors = [(0, green, 0) for green in range(256)]
        cache = {}
        for char in self.katakana_symbols:
            rendered = {(char, color): self.font.render(char, True, color) for color in colors}
            cache.update(rendered)
        return cache

    def update(self):
        current_time = pg.time.get_ticks()
        self.change_symbols(current_time)
        self.scroll_columns(current_time)
        self.render()

    def scroll_columns(self, current_time):
        columns_to_shift = np.argwhere(current_time % self.column_speeds == 0)
        columns_to_shift = columns_to_shift[:, 1]
        unique_columns = np.unique(columns_to_shift)
        self.matrix[:, unique_columns] = np.roll(self.matrix[:, unique_columns], shift=1, axis=0)

    def change_symbols(self, current_time):
        positions_to_change = np.argwhere(current_time % self.char_intervals == 0)
        new_symbols = np.random.choice(self.katakana_symbols, positions_to_change.shape[0])
        self.matrix[positions_to_change[:, 0], positions_to_change[:, 1]] = new_symbols

    def render(self):
        frame_pixels = self.capture_camera_frame()
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                if char:
                    position = x * self.FONT_SIZE, y * self.FONT_SIZE
                    _, red, green, blue = pg.Color(frame_pixels[position])
                    if red and green and blue:
                        avg_color = (red + green + blue) // 3
                        avg_color = 220 if 160 < avg_color < 220 else avg_color
                        char_image = self.rendered_chars_cache[(char, (0, avg_color, 0))]
                        char_image.set_alpha(avg_color + 60)
                        self.vision_app.surface.blit(char_image, position)


class MatrixCameraEffect:
    def __init__(self):
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 960, 720
        pg.init()
        self.display = pg.display.set_mode(self.RESOLUTION)
        self.surface = pg.Surface(self.RESOLUTION)
        self.fps_clock = pg.time.Clock()
        self.matrix_effect = MatrixEffect(self)

        pygame.camera.init()
        self.camera = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.camera.start()

    def render(self):
        self.surface.fill(pg.Color('black'))
        self.matrix_effect.update()
        self.display.blit(self.surface, (0, 0))

    def mainloop(self):
        while True:
            self.render()
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            pg.display.flip()
            self.fps_clock.tick(30)


if __name__ == '__main__':
    matrix_vision_app = MatrixCameraEffect()
    matrix_vision_app.mainloop()
"""
