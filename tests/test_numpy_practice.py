import pytest
import numpy as np
from src import numpy_practice


@pytest.mark.describe('three_zeros()')
@pytest.mark.it('It should be a function')
def test_three_zeros_function():
    result = numpy_practice.three_zeros
    assert result


@pytest.mark.describe('three_zeros()')
@pytest.mark.it('It should return a numpy array containing three zeros')
def test_three_zeros_contains():
    result = numpy_practice.three_zeros()
    assert type(result) == np.ndarray
    assert type(result[0]) == np.float64
    assert (result == [0., 0., 0.]).all()


@pytest.mark.describe('five_zeros()')
@pytest.mark.it('It should be a function')
def test_five_zeros_function():
    result = numpy_practice.five_zeros
    assert result


@pytest.mark.describe('five_zeros()')
@pytest.mark.it('It should return a numpy array containing five zeros')
def test_five_zeros():
    result = numpy_practice.five_zeros()
    assert (result == [0., 0., 0., 0., 0.]).all()
    assert type(result) == np.ndarray
    assert type(result[0]) == np.float64


@pytest.mark.describe('array_shape()')
@pytest.mark.it('It should be a function')
def test_array_shape_function():
    result = numpy_practice.array_shape
    assert result


@pytest.mark.describe('array_shape()')
@pytest.mark.it('It should return the shape of a numpy array')
def test_array_shape():
    test_array = np.zeros(10)
    result = numpy_practice.array_shape(test_array)
    assert result == (10,)


@pytest.mark.describe('reshape_array()')
@pytest.mark.it('It should be a function')
def test_reshape_array_function():
    result = numpy_practice.reshape_array
    assert result


@pytest.mark.describe('reshape_array()')
@pytest.mark.it('It should return a reshaped numpy array')
def test_reshape_array():
    test_array = np.zeros(10)
    result = numpy_practice.reshape_array(test_array, (5, 2))
    assert result.shape == (5, 2)
