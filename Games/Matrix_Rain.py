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

# Represents a matrix of binary numbers that updates its columns and characters over time.
class BinaryMatrix:
    def __init__(self, display, font_size=8):
        # Initialization method

        # Reference to the display object which is an instance of MatrixDisplay.
        self.display = display
        # Font size for displaying binary numbers.
        self.FONT_SIZE = font_size
        # Determine the number of rows and columns based on display dimensions and font size.
        self.SIZE = self.ROWS, self.COLS = display.HEIGHT // font_size, display.WIDTH // font_size
        # Define the font to be used.
        self.font = pg.font.Font(None, font_size, bold=True)
        
        # Initialize the matrix with random 0s and 1s.
        self.matrix = np.random.choice([0, 1], self.SIZE)
        # Random intervals at which each character changes.
        self.char_intervals = np.random.randint(25, 50, size=self.SIZE)
        # Random speeds for each column's downward movement.
        self.cols_speed = np.random.randint(1, 500, size=self.SIZE)

    def get_frame(self):
        # Fetches the current frame from the camera.
        image = self.display.cam.get_image()
        return pg.pixelarray.PixelArray(image)

    def run(self):
        # Main method to handle matrix updates and rendering.

        # Get current number of milliseconds since pygame was initialized.
        frames = pg.time.get_ticks()
        # Update characters and column positions.
        self.charsChange(frames)
        self.columnChange(frames)
        # Render the matrix.
        self.draw()

    def columnChange(self, frames):
        # Modifies the position of columns based on the given frame count.

        # Determine columns that need to shift based on the current frame count.
        num_cols = np.argwhere(frames % self.cols_speed == 0)
        num_cols = num_cols[:, 1]
        # Roll (move) the columns downward.
        self.matrix[:, num_cols] = np.roll(self.matrix[:, num_cols], shift=1, axis=0)

    def charsChange(self, frames):
        # Updates characters in the matrix based on the given frame count.

        # Determine which characters need to change based on the current frame count.
        mask = np.argwhere(frames % self.char_intervals == 0)
        # Update the characters in the matrix.
        self.matrix[mask[:, 0], mask[:, 1]] = np.random.choice([0, 1], mask.shape[0])

    def draw(self):
        # Renders the matrix on the display surface.

        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                # Calculate the on-screen position for the character.
                pos = x * self.FONT_SIZE, y * self.FONT_SIZE
                # Render the character as an image.
                char_image = self.font.render(str(char), True, (0, 255, 0))
                # Blit (draw) the character image onto the display's surface.
                self.display.surface.blit(char_image, pos)

# Represents the main application window that displays the matrix.
class MatrixDisplay:
    def __init__(self):
        # Initialization method

        # Define the resolution of the application window.
        self.RES = self.WIDTH, self.HEIGHT = 960, 720
        # Initialize pygame.
        pg.init()
        # Create the main screen (window).
        self.screen = pg.display.set_mode(self.RES)
        # Create a drawing surface.
        self.surface = pg.Surface(self.RES)
        # Clock for controlling frame rate.
        self.clock = pg.time.Clock()
        # Instantiate the binary matrix.
        self.matrix = BinaryMatrix(self)
        
        # Initialize the camera module.
        pygame.camera.init()
        # Connect to the default camera.
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.cam.start()

    def draw(self):
        # Handles all drawing operations.

        # Fill the surface with a black color.
        self.surface.fill(pg.Color('black'))
        # Update and draw the matrix.
        self.matrix.run()
        # Draw the surface onto the main screen.
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        # Main loop for the application.

        while True:
            # Draw contents onto the screen.
            self.draw()
            # Handle window close events.
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            # Update the actual display.
            pg.display.flip()
            # Limit the loop to 30 frames per second.
            self.clock.tick(30)

if __name__ == '__main__':
    # If this script is the main program, instantiate the display and run the application.
    displayApp = MatrixDisplay()
    displayApp.run()


"""
