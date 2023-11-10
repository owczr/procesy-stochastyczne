import os

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


LIMIT = 1000
RESOLUTION = 1.66 ** 2
IMAGE_PATH = 'image1.tif'
OUTPUT_PATH = 'montecarlo.png'


def generate_points(x_lim, y_lim):
    x = np.random.randint(0, x_lim)
    y = np.random.randint(0, y_lim)
    return x, y


def read_image(path):
    return np.array(Image.open(path).convert('L'))


def save_image(points_hit, points_missed, image, name):
    plt.imshow(image, cmap='gray')
    plt.scatter(*zip(*points_hit), c='g')
    plt.scatter(*zip(*points_missed), c='r')
    plt.savefig(name)
    print(f"Output image saved to {name}")
    


def run():
    image = read_image(IMAGE_PATH)

    image_max = np.max(image)

    y_lim, x_lim = image.shape

    area_estimate = 0

    points_hit = []
    points_missed = []

    print("Estimating area...")

    for idx in range(LIMIT):
        x, y = generate_points(x_lim, y_lim)

        if image[y, x] == image_max:
            area_estimate = area_estimate + 1
            points_hit.append((x, y))
        else:
            points_missed.append((x, y))
    
    area_estimate = area_estimate / RESOLUTION

    print(f"Estimated area for {LIMIT} points with resolution {RESOLUTION} PPI is {area_estimate:.4f}cm")

    save_image(points_hit, points_missed, image, OUTPUT_PATH)



if __name__ == "__main__":
    run()
