import otsu
import numpy as np
from PIL import Image
import sys

def neighbors(row, col, image_width, image_height):
    neighborhood = []
    # directly right
    if col < image_width - 1:
        neighborhood.append((row, col + 1))
    if row < image_height - 1:
        # directly below
        neighborhood.append((row + 1, col))
        if col < image_width - 1:
            # down and right
            neighborhood.append((row + 1, col + 1))
        if col > 0:
            # down and left
            neighborhood.append((row, col - 1))
            neighborhood.append((row + 1, col - 1))
    if row > 0:
        if col < image_width - 1:
            neighborhood.append((row - 1, col + 1))
        if col > 0:
            neighborhood.append((row - 1, col - 1))
    return neighborhood

def search(label_image, label_num, row, col):
    label_image[row][col] = label_num
    neighbor_set = neighbors(row, col, label_image.shape[1], label_image.shape[0])
    for neighbor_row, neighbor_col in neighbor_set:
        if label_image[neighbor_row][neighbor_col] == -1:
            search(label_image, label_num, neighbor_row, neighbor_col)

def find_component(label_image, label_num):
    for row in range(label_image.shape[0]):
        for col in range(label_image.shape[1]):
            if label_image[row][col] == -1:
                label_num = label_num + 1
                search(label_image, label_num, row, col)
    return label_image, label_num

def recursive_connected_components(image):
    label_image = (1 - image) * -1
    label = 0
    label_image, num_objects = find_component(label_image, label)
    return label_image, num_objects


sys.setrecursionlimit(50000)
np.set_printoptions(threshold=sys.maxsize)
if __name__ == '__main__':
    print("label_objects_binary_image file")

    # image = otsu.create_otsu_binary("SingleSquare.png", as_array=True)
    # image = otsu.create_otsu_binary("TestSquaresWithHoles.jpg", as_array=True)
    image = otsu.create_otsu_binary("three_shapes.png", as_array=True)

    label_image, num_objects = recursive_connected_components(image)


