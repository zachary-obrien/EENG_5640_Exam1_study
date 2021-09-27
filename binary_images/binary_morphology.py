import numpy as np


def buffer(image, mask, value=0):
    buffer_width = int((mask.shape[1] - 1) / 2)
    buffer_height = int((mask.shape[0] - 1) / 2)

    height_array = np.full(shape=(image.shape[0], buffer_height), fill_value=value)
    # add to top and bottom
    image = np.append(image, height_array, 1)
    image = np.append(height_array, image, 1)

    # add to left and right
    width_array = np.zeros((buffer_width, image.shape[1]))
    image = np.append(image, width_array, 0)
    image = np.append(width_array, image, 0)
    return image, (buffer_width, buffer_height)


def dilation(image, kernal_size):
    mask = np.full(shape=(kernal_size, kernal_size), fill_value=1)
    buffer_image, (buffer_width, buffer_height) = buffer(image, mask)

    matricies = []
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            if image[row][col] == 1:
                buffer_image[row:(row + mask.shape[0]), col:(col+mask.shape[1])] = mask

    dilated_image = buffer_image[buffer_height:(buffer_image.shape[0]-buffer_height), buffer_width:(buffer_image.shape[1]-buffer_width)]

    return dilated_image

def erosion(image, kernal_size):

    mask = np.full(shape=(kernal_size, kernal_size), fill_value=1)
    buffer_image, (buffer_width, buffer_height) = buffer(image, mask)

    eroded_image = np.zeros(shape=image.shape)
    for row in range(buffer_height, image.shape[0] + buffer_height):
        for col in range(buffer_width, image.shape[1] + buffer_width):
            sub_matrix = buffer_image[(row - buffer_height):(row + buffer_height + 1), (col - buffer_width):(col + buffer_width + 1)]
            if np.array_equal(sub_matrix, mask):
                eroded_image[row - buffer_height][col - buffer_width] = 1

    return eroded_image


def closing(image, kernal_size):
    closed_image = erosion(dilation(image, kernal_size), kernal_size)
    return closed_image

def opening(image, kernal_size):
    closed_image = dilation(erosion(image, kernal_size), kernal_size)
    return closed_image


if __name__ == '__main__':

    test_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 0],
                            [0, 0, 0, 1, 1, 1, 1, 0],
                            [0, 0, 0, 1, 1, 1, 1, 0],
                            [0, 0, 1, 1, 1, 1, 1, 0],
                            [0, 0, 0, 1, 1, 1, 1, 0],
                            [0, 0, 1, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]).astype(np.float64)
    print("original")
    print(test_matrix)
    print("dilated")
    print(dilation(test_matrix, 3))
    print("eroded")
    print(erosion(test_matrix, 3))
    print("closed")
    print(closing(test_matrix, 3))
    print("opened")
    print(opening(test_matrix, 3))

