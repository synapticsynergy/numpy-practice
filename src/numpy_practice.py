import numpy as np


def three_zeros():
    return np.zeros(3)


def five_zeros():
    return np.zeros(5)


def seven_ones():
    return np.ones(7)


def convert_to_nparray(array):
    print(np.array(array).ndim)
    return np.array(array)


def array_shape(np_array):
    return np_array.shape


def get_dimensions(np_array):
    return np_array.ndim


def reshape_array(np_array, shape):
    np_array.shape = shape
    return np_array


def get_linspace(start, stop, num):
    print(np.linspace(start, stop, num))
    return np.linspace(start, stop, num)
