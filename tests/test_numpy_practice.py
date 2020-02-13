import pytest
import numpy as np
from src import numpy_practice


def test_three_zeros():
    result = numpy_practice.three_zeros()
    assert (result == [0., 0., 0.]).all()
    assert type(result) == np.ndarray
    assert type(result[0]) == np.float64


def test_five_zeros():
    result = numpy_practice.five_zeros()
    assert (result == [0., 0., 0., 0., 0.]).all()
    assert type(result) == np.ndarray
    assert type(result[0]) == np.float64


def test_array_shape():
    test_array = np.zeros(10)
    result = numpy_practice.array_shape(test_array)
    assert result == (10,)


def test_reshape_array():
    test_array = np.zeros(10)
    result = numpy_practice.reshape_array(test_array, (5, 2))
    assert result == (5, 2)
