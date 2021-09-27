import math

import numpy as np


def prewitt_operator(image):
    buffer_width = 1
    buffer_height = 1

    prewitt_f = np.array([[-1, 0, 1],
                          [-1, 0, 1],
                          [-1, 0, 1]])

    prewitt_g = np.array([[1, 1, 1],
                          [0, 0, 0],
                          [-1, -1, -1]])

    prewitt_f_image = np.copy(image)
    prewitt_g_image = np.copy(image)

    for row in range(buffer_height, image.shape[1] - buffer_height):
        for col in range(buffer_width, image.shape[1] - buffer_width):
            sub_matrix = image[row - 1:row + 2,
                         col - 1:col + 2]

            f_matrix = np.multiply(prewitt_f, sub_matrix)
            f_prewitt = np.sum(f_matrix) / 6
            g_matrix = np.multiply(prewitt_g, sub_matrix)
            g_prewitt = np.sum(g_matrix) / 6

            prewitt_mag = math.sqrt(((f_prewitt ** 2) + (g_prewitt ** 2)))
            prewitt_dir =

