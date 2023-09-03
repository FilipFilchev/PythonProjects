from manim import *
import numpy as np

class MandelbrotScene(Scene):
    def construct(self):
        # Dimensions
        WIDTH, HEIGHT = 800, 800
        RE_START, RE_END = -2, 2
        IM_START, IM_END = -2, 2

        # Create an empty image
        mandelbrot_image = ImageMobject(np.uint8(np.zeros((HEIGHT, WIDTH, 3))))
        self.add(mandelbrot_image)

        for i in range(1, 50):  # You can increase the range for more iterations
            self.update_mandelbrot_image(mandelbrot_image, i)
            self.wait(0.1)  # Adjust for desired delay between frames

    def update_mandelbrot_image(self, image_mobject, iterations):
        # Dimensions
        WIDTH, HEIGHT = image_mobject.pixel_array.shape[1], image_mobject.pixel_array.shape[0]
        RE_START, RE_END = -2, 2
        IM_START, IM_END = -2, 2

        # Generate Mandelbrot set image for a given number of iterations
        mandelbrot_array = np.zeros((HEIGHT, WIDTH, 4))  # Notice the 4 here for RGBA
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                zx, zy = x * (RE_END - RE_START) / (WIDTH - 1) + RE_START, y * (IM_END - IM_START) / (HEIGHT - 1) + IM_START
                c = zx + zy * 1j
                z = c
                for i in range(iterations):
                    if abs(z) > 2.0:
                        break 
                    z = z * z + c
                # Convert iteration number to an RGBA color
                r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
                mandelbrot_array[y, x] = (r, g, b, 255)  # 255 for full opacity

        # Update image data
        image_mobject.pixel_array[:, :, :] = np.uint8(mandelbrot_array)
        image_mobject.update()


if __name__ == "__main__":
    from manim import *

    # Run the Scene
    config.pixel_height = 800
    config.pixel_width = 800
    config.frame_height = 8.0
    config.frame_width = 8.0
    SceneClass = MandelbrotScene
    scene = SceneClass()
    scene.render()
    scene.play(SceneClass().construct())

#manim -pql MandelbrotSet.py MandelbrotScene