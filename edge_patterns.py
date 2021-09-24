from PIL import Image
import numpy as np
import otsu

external_patterns = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
internal_patterns = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1]]

#Only takes color (greyscale=False) and greyscale(greyscale=True) images
def load_image(img_filename, greyscale=False):
    otsu.create_otsu_binary(img_filename, greyscale)

def num_holes(image):
    row_size = image.shape[0]
    col_size = image.shape[1]
    external_corners = 0
    internal_corners = 0
    for index_row, row in enumerate(image):
        for index_col, col in enumerate(row):
            if index_row < row_size - 1 and index_col < col_size -1:
                pattern = [image[index_row, index_col], image[index_row, index_col + 1],
                            image[index_row + 1, index_col], image[index_row + 1, index_col + 1]]
                if pattern in external_patterns:
                    external_corners = external_corners + 1
                elif pattern in internal_patterns:
                    internal_corners = internal_corners + 1
    return int((external_corners - internal_corners) / 4)