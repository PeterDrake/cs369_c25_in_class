import numpy as np

data = np.array([[1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]])

kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

def convolve(data, kernel, r, c):
    field = data[r-1:r+2, c-1:c+2]
    return np.sum(field * kernel

print(convolve(data, kernel, 2, 5))
