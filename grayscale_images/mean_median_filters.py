import numpy as np
from extend_matrix import buffer

def mean_filter(image, mask):
    output_image = np.copy(image)
    buffer_width = int((mask.shape[1] - 1) / 2)
    buffer_height = int((mask.shape[0] - 1) / 2)

    for row in range(buffer_height, image.shape[0]-buffer_height):
        for col in range(buffer_width, image.shape[1]-buffer_width):
            sub_matrix = image[row-buffer_height:row+buffer_height+1,
                         col-buffer_width:col+buffer_width+1]
            output_image[row][col] = np.mean(sub_matrix)
    return output_image

def median_filter(image, mask):
    output_image = np.copy(image)
    buffer_width = int((mask.shape[1] - 1) / 2)
    buffer_height = int((mask.shape[0] - 1) / 2)

    for row in range(buffer_height, image.shape[0]-buffer_height):
        for col in range(buffer_width, image.shape[1]-buffer_width):
            sub_matrix = image[row-buffer_height:row+buffer_height+1,
                         col-buffer_width:col+buffer_width+1]
            output_image[row][col] = np.median(sub_matrix)
    return output_image


if __name__ == '__main__':
    test_matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                            [1, 1, 1, 1, 1, 1, 1, 7],
                            [2, 0, 0, 1, 1, 1, 1, 6],
                            [3, 0, 0, 1, 1, 1, 1, 5],
                            [4, 0, 1, 1, 1, 1, 1, 4],
                            [5, 0, 0, 1, 1, 1, 1, 3],
                            [6, 0, 1, 1, 0, 0, 0, 2],
                            [9, 8, 7, 6, 5, 4, 3, 2]]).astype(np.float64)

    mask = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]])

    mask = np.array([[1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1]])

    zero_row = buffer(test_matrix, mask=mask, value="extend")
    print("buffer\n", zero_row)
    mean_row = np.rint(mean_filter(zero_row, mask))
    print("mean_row\n", mean_row)

    median_row = np.rint(median_filter(zero_row, mask))
    print("median_row\n", median_row)