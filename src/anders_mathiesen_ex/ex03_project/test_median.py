# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'


import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError("Can find median of a empty list")
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_one_element():
    test_list = [1]
    median_list = median(test_list)
    assert median_list == 1


def test_odd_and_ordered():
    test_list = [1, 2, 3]
    median_list = median(test_list)
    assert median_list == 2


def test_even_and_reverse_ordered():
    test_list = [2, 1]
    median_list = median(test_list)
    assert median_list == 1.5


def test_empty_list():
    test_list = []
    with pytest.raises(ValueError):
        _ = median(test_list)


def test_original_unchanged():
    single_list = [4, 2, 3]
    _ = median(single_list)
    assert [4, 2, 3] == single_list


