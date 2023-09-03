import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def create_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            x = x_vals[j]
            y = y_vals[i]
            c = x + y * 1j
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)

    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set, xmin, xmax, ymin, ymax):
    plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax), cmap='hot', aspect='equal')
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.show()

# Parameters
width = 800
height = 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 100

# Create Mandelbrot set
mandelbrot_set = create_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)

# Plot Mandelbrot set
plot_mandelbrot(mandelbrot_set, xmin, xmax, ymin, ymax)
