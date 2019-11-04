# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.r = seed

    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.r = (a*self.r) % m
        return self.r


class ListRand:
    def __init__(self, list_number):
        self.list_number = list_number
        self.counter = 0

    def rand(self):
        if len(self.list_number) == self.counter:
            raise RuntimeError('Out of range')
        number = self.list_number[self.counter]
        self.counter += 1
        return number


if __name__ == "__main__":
    lcg = LCGRand(4)
    for _ in range(5):
        print(lcg.rand())
    rand = [3, 5, 3, 6]
    list_rand = ListRand(rand)
    for _ in range(len(rand)+1):
        print(list_rand.rand())
