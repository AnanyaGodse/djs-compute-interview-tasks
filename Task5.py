import numpy as np


def arrays(arr):
    np_arr = np.array(arr, float)
    np_arr = np.flip(np_arr)
    return np_arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
