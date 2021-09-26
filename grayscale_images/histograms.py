import numpy as np
from PIL import Image

def load_image(img_filename, greyscale=False):
    image = Image.open(img_filename)
    if not greyscale:
        image = image.convert('L')
    image_array = np.asarray(image)
    return image_array


def make_histogram(image):
    histogram = {}
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            if image[row][col] not in histogram.keys():
                image[row][col] = 0
            image[row][col] = image[row][col] + 1

    return histogram


