from PIL import Image
import numpy as np
import otsu

internal_patterns = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
external_patterns = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]

#Only takes color (greyscale=False) and greyscale(greyscale=True) images
def load_image(img_filename, greyscale=False):
    image = otsu.create_otsu_binary(img_filename, greyscale)
    image.show()
    return np.asarray(image) / 255

def num_corners(image):
    row_size = image.shape[0]
    col_size = image.shape[1]
    external_corners = 0
    internal_corners = 0
    num_checks = 0
    pattern = None
    for index_row, row in enumerate(image):
        for index_col, col in enumerate(row):
            if index_row < row_size - 1 and index_col < col_size -1:
                num_checks = num_checks + 1
                pattern = [image[index_row, index_col], image[index_row, index_col + 1],
                            image[index_row + 1, index_col], image[index_row + 1, index_col + 1]]
                if pattern in external_patterns:
                    external_corners = external_corners + 1
                elif pattern in internal_patterns:
                    internal_corners = internal_corners + 1
    print("Final Pattern", pattern)
    print("External Patterns", external_patterns)
    print("Internal Patterns", internal_patterns)
    print("num checks", num_checks)
    print("external corners", external_corners)
    print("internal corners", internal_corners)
    return int((external_corners - internal_corners) / 4)

def count_objects(image_name):
    image = load_image(image_name)
    return num_corners(image)

# print("found", count_objects("TestSquaresWithHoles.jpg"), "object")
# print("found", count_objects("singleSquare.png"), "object")
print("found", count_objects("single_square_full.png"), "object")