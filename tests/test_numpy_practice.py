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


@pytest.mark.describe('seven_ones()')
@pytest.mark.it('It should be a function')
def test_seven_ones_function():
    result = numpy_practice.seven_ones
    assert result


@pytest.mark.describe('seven_ones()')
@pytest.mark.it('It should return a numpy array containing five zeros')
def test_seven_ones():
    result = numpy_practice.seven_ones()
    assert (result == [1., 1., 1., 1., 1., 1., 1.]).all()
    assert type(result) == np.ndarray
    assert type(result[0]) == np.float64


@pytest.mark.describe('convert_to_nparray()')
@pytest.mark.it('It should be a function')
def test_convert_to_nparray_function():
    result = numpy_practice.convert_to_nparray
    assert result


@pytest.mark.describe('convert_to_nparray()')
@pytest.mark.it('It should accept a list and return a matching numpy array')
def test_convert_to_nparray():
    test_list = [1, 2, 3, 4, 5]
    result = numpy_practice.convert_to_nparray(test_list)
    assert (result == test_list).all()


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


@pytest.mark.describe('get_dimensions()')
@pytest.mark.it('It should be a function')
def test_get_dimensions_function():
    result = numpy_practice.get_dimensions
    assert result


@pytest.mark.describe('get_dimensions()')
@pytest.mark.it('It should return a reshaped numpy array')
def test_get_dimensions():
    test_array = [[[[[[[[1, 2, 3]]]]]]]]
    result = numpy_practice.get_dimensions(np.array(test_array))
    assert result == 8


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


@pytest.mark.describe('get_linspace()')
@pytest.mark.it('It should be a function')
def test_get_linspace_function():
    result = numpy_practice.get_linspace
    assert result


@pytest.mark.describe('get_linspace()')
@pytest.mark.it('It should return a numpy array that specifies the possible start and end numbers, and number of elements to return')
def test_get_linspace_nparray():
    result = numpy_practice.get_linspace(5, 20, 9)
    assert (result == [5., 6.875, 8.75, 10.625,
                       12.5, 14.375, 16.25, 18.125, 20.]).all()
