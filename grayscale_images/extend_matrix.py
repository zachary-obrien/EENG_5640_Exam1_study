import numpy as np


def buffer(image, mask=None, value="zeroes"):
    if mask is None:
        return image
    elif value == "zeroes" or value == "extend":
        buffer_width = int((mask.shape[1] - 1) / 2)
        buffer_height = int((mask.shape[0] - 1) / 2)

        height_array = np.full(shape=(image.shape[0], buffer_height), fill_value=0)
        # add to top and bottom
        new_image = np.append(image, height_array, 1)
        new_image = np.append(height_array, new_image, 1)

        # add to left and right
        width_array = np.zeros((buffer_width, new_image.shape[1]))
        new_image = np.append(new_image, width_array, 0)
        new_image = np.append(width_array, new_image, 0)

        if value == "extend":
            print("fill with values")
            top_left = np.full(shape=(buffer_width), fill_value=[image[0][0]])
            top_right = np.full(shape=(buffer_width), fill_value=[image[0][-1]])
            bottom_left = np.full(shape=(buffer_width), fill_value=[image[-1][0]])
            bottom_right = np.full(shape=(buffer_width), fill_value=[image[-1][-1]])
            top_row = np.concatenate([top_left, image[0], top_right])
            bottom_row = np.concatenate([bottom_left, image[-1], bottom_right])
            left_col = np.concatenate([top_left, image[:,0], bottom_left])
            right_col = np.concatenate([top_right, image[:,-1], bottom_right])
            for row in range(-buffer_height,buffer_height):
                if row < 0:
                    new_image[row] = bottom_row
                else:
                    new_image[row] = top_row
            for col in range(-buffer_width, buffer_width):
                if col < 0:
                    new_image[:,col] = right_col
                else:
                    new_image[:,col] = left_col

        return new_image



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
    same_row = buffer(test_matrix)
    print("no mask")
    print(same_row)

    zero_row = buffer(test_matrix, mask=mask, value="zeroes")
    print("Zero Row")
    print(zero_row)

    ext_row = buffer(test_matrix, mask=mask, value="extend")
    print("extend Row")
    print(ext_row)

    print("rows")
    print()