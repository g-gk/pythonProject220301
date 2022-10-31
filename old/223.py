import numpy as np
from PIL import Image


def bw_convert():
    img = Image.open('image.jpg')
    image = np.asarray(img)
    k = np.array([0.2989, 0.587, 0.114])
    sums = np.round(np.sum(image * k, axis=2)).astype(np.uint8)
    ar2 = np.repeat(sums, 3).reshape(image.shape)
    Image.fromarray(ar2).save('res.jpg')


bw_convert()
