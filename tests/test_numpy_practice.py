import pytest
import numpy as np
from src import numpy_practice


def test_three_zeros():
    result = numpy_practice.three_zeros()
    assert (result == [0., 0., 0.]).all()
