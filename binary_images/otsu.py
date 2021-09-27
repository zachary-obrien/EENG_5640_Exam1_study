import numpy as np
from PIL import Image

def load_image(img_filename, greyscale=True):
    image = Image.open(img_filename)
    if not greyscale:
        image = image.convert('L')
    image_array = np.asarray(image)
    return image_array

def otsu(grey):
    pixel_number = grey.shape[0] * grey.shape[1]
    mean_weight = 1.0/pixel_number
    his, bins = np.histogram(grey, np.arange(256))
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(255)
    for t in bins[1:-1]: # This goes from  1 to 254 uint8 range (Pretty sure wont be those values)
        pcb = np.sum(his[:t])
        pcf = np.sum(his[t:])
        Wb = pcb * mean_weight
        Wf = pcf * mean_weight

        mub = np.sum(intensity_arr[:t]*his[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:]*his[t:]) / float(pcf)
        if pcf == 0:
            print("pcf", pcf)
            print("muf", muf)
            print("his", his)
        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    final_img = grey.copy()
    final_img[grey > final_thresh] = 1
    final_img[grey < final_thresh] = 0
    return final_img


def create_otsu_binary(image_name, greyscale=False, as_array=False):
    final_image = otsu(load_image(image_name, greyscale))
    if not as_array:
        final_image = Image.fromarray(final_image * 255)
    return final_image


if __name__ == '__main__':
    print("Otsu file")
    image = create_otsu_binary("EDTem.jpg")
    image.show()

