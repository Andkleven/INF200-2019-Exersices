# -*- coding: utf-8 -*-


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    squares_by_list = []
    for k in range(n):
        if k % 3 == 1:
            squares_by_list.append(k**2)
    return squares_by_list
