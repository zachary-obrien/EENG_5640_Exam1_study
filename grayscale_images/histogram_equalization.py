import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def load_image(img_filename, greyscale=False):
    image = Image.open(img_filename)
    if not greyscale:
        image = image.convert('L')
    image_array = np.asarray(image)
    return image_array


def make_histogram(flattened_image, bins):
    out_histogram = np.zeros(bins)
    for entry in flattened_image:
        out_histogram[entry] = out_histogram[entry] + 1
    return out_histogram


def cdf(histogram):
    print("CDF")
    densities = [histogram[0]]
    for number in histogram[1:]:
        densities.append(densities[-1] + number)
    densities = np.array(densities)
    return densities


def cdf_new(densities):
    new_cdf = ((densities - densities.min()) * 255 / (densities.max() - densities.min())).astype('uint8')
    return new_cdf


def equalize_histogram(image_name, intensity_range):
    image = load_image(image_name)
    plt.imshow(image, cmap='gray')
    plt.show()
    flat_image = image.flatten()

    histogram = make_histogram(flat_image, intensity_range)
    cdf_list = cdf(histogram)
    new_cdf = cdf_new(cdf_list)

    new_image = new_cdf[flat_image]
    new_image = np.reshape(new_image, image.shape)
    plt.imshow(new_image, cmap='gray')
    plt.show()


if __name__ == '__main__':
    equalize_histogram("../chest_xray.jpeg", 256)
