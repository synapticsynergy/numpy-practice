import numpy as np


def three_zeros():
    return np.zeros(3)


def five_zeros():
    return np.zeros(5)


def array_shape(np_array):
    return np_array.shape


def reshape_array(np_array, shape):
    np_array.shape = shape
    return np_array.shape
