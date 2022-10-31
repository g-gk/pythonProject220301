import numpy as np

from PIL import Image


def bw_convert():
    im = Image.open('image.jpg')
    arr = np.asarray(im, dtype='uint8')
    k = np.array([[[0.2989, 0.587, 0.114]]])
    sums = np.round(np.sum(arr * k, axis=2)).astype(np.uint8)
    arr2 = np.repeat(sums, 3).reshape(arr.shape)
    im2 = Image.fromarray(arr2)
    im2.save('res.jpg')
