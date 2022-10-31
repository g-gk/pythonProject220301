import numpy as np
from PIL import Image


def bw_convert():
    x = np.asarray(Image.open('image.jpg'), dtype='uint8')
    y = np.array([[[0.2989, 0.587, 0.114]]])
    solution = np.round(np.sum(x * y, axis=2)).astype(np.uint8)
    solution2 = np.repeat(solution, 3).reshape(x.shape)
    Image.fromarray(solution2).save('res.jpg')
