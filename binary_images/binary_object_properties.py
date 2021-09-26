from label_objects_binary_image import recursive_connected_components
from otsu import create_otsu_binary
import math

def check_neighbors(labeled_image, row, col):
    row_mod = [-1, 0, 1]
    col_mod = [-1, 0, 1]
    for neighbor_row in row_mod:
        for neighbor_col in col_mod:
            possible_row = row - neighbor_row
            possible_col = col - neighbor_col
            if possible_row != -1 and possible_row != labeled_image.shape[0] and possible_col != -1 and \
                    possible_col != labeled_image.shape[1]:
                if labeled_image[possible_row][possible_col] == 0:
                    return True
    return False

def find_perimeter(labeled_image):
    perimeter_sizes = {}
    for row in range(labeled_image.shape[0]):
        for col in range(labeled_image.shape[1]):
            if labeled_image[row][col] != 0 and check_neighbors(labeled_image, row, col):
                if labeled_image[row][col] not in perimeter_sizes.keys():
                    perimeter_sizes[labeled_image[row][col]] = (0, [])
                size, points = perimeter_sizes[labeled_image[row][col]]
                points.append((row, col))
                perimeter_sizes[labeled_image[row][col]] = (size + 1, points)
    return perimeter_sizes


def find_area(labeled_image):
    sizes = {}
    for row in range(labeled_image.shape[0]):
        for col in range(labeled_image.shape[1]):
            if labeled_image[row][col] != 0:
                if labeled_image[row][col] not in sizes.keys():
                    sizes[labeled_image[row][col]] = 0
                sizes[labeled_image[row][col]] = sizes[labeled_image[row][col]] + 1
    return sizes

def find_centroids(labeled_image):
    area_points = {}
    for row in range(labeled_image.shape[0]):
        for col in range(labeled_image.shape[1]):
            if labeled_image[row][col] != 0:
                if labeled_image[row][col] not in area_points.keys():
                    area_points[labeled_image[row][col]] = []
                area_points[labeled_image[row][col]].append((row, col))
    centroids = {}
    for shape in area_points.keys():
        total_rows = 0
        total_cols = 0
        for (row, col) in area_points[shape]:
            total_rows = total_rows + row
            total_cols = total_cols + col
        r = round((total_rows / len(area_points[shape])), 10)
        c = round((total_cols / len(area_points[shape])), 10)
        centroids[shape] = (r, c)
    return centroids

def find_circularity(perimeter_points, centroid):
    perm_len = len(perimeter_points)
    sum_radial = 0
    std_radial = 0
    for point_row, point_col in perimeter_points:
        distance = math.sqrt(((point_row - centroid[0]) ** 2) + ((point_col - centroid[0]) ** 2))
        sum_radial = sum_radial + distance
    mu = sum_radial / perm_len

    for point_row, point_col in perimeter_points:
        distance = math.sqrt(((point_row - centroid[0]) ** 2) + ((point_col - centroid[0]) ** 2))
        std_radial = std_radial + ((distance - mu) ** 2)
    sigma = math.sqrt(std_radial / perm_len)
    return round((mu / sigma), 10)


if __name__ == '__main__':
    print("binary_object_properties file"
          ".")
    binary_image = create_otsu_binary("three_shapes.png", as_array=True)
    labeled_image, num_objects = recursive_connected_components(binary_image)
    perimeter_list = find_perimeter(labeled_image)
    area_list = find_area(labeled_image)
    centroids = find_centroids(labeled_image)

    for label in perimeter_list.keys():
        print("-------- Shape", label, "--------")
        print("Shape Number:", label, "Area is:", area_list[label])
        print("Shape Number:", label, "Centroid is:", centroids[label])
        print("Shape Number:", label, "Perimeter is:", perimeter_list[label][0], "Point list len:", len(perimeter_list[label][1]))
        print("Shape Number:", label, "Circularity is:", find_circularity(perimeter_list[label][1], centroids[label]))
        print()

