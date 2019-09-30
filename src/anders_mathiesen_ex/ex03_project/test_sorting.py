# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'


import random


def sort_list(list_data):
    new_data = list(list_data)
    for number in range(len(list_data)):
        if number == len(list_data) - 1:
            break
        first_number = new_data[number]
        second_number = new_data[number + 1]
        if first_number > second_number:
            new_data[number] = second_number
            new_data[number + 1] = first_number
    return new_data


def bubble_sort(random_list):
    for _ in range(len(random_list)):
        random_list = sort_list(random_list)
    return list(tuple(random_list))


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    sorted_list = bubble_sort(empty_list)
    assert sorted_list == empty_list


def test_single():
    """Test that the sorting function works for single-element list"""
    single_list = [1]
    sorted_list = bubble_sort(single_list)
    assert sorted_list == single_list


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    single_list = [3, 2, 1]
    sorted_list = bubble_sort(single_list)
    assert sorted_list != single_list


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    single_list = [4, 2, 3]
    _ = bubble_sort(single_list)
    assert [4, 2, 3] == single_list


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    single_list = [1, 2, 3]
    sorted_list = bubble_sort(single_list)
    assert sorted_list == single_list


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    single_list = [1, 2, 5, 7]
    reverse_list = single_list.copy()
    reverse_list.reverse()
    sorted_list = bubble_sort(reverse_list)
    assert sorted_list == single_list


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    single_list = [1, 1, 1]
    sorted_list = bubble_sort(single_list)
    assert single_list == sorted_list


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    random_list = [random.randint(1, 500) for _ in range(random.randint(1, 100))]
    test_sorted_list = random_list.copy()
    test_sorted_list = sorted(test_sorted_list)
    sorted_list = bubble_sort(random_list)
    assert sorted_list == test_sorted_list
