# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'

import random


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None
        self.is_iter = False

    def __iter__(self):
        self.is_iter = True
        return self

    def __next__(self):
        if self.is_iter:
            raise RuntimeError
        if self.num_generated_numbers <= self.length:
            raise StopIteration
        self.num_generated_numbers += 1
        return self.generator


class LCGRand:
    def __init__(self, seed):
        self.steps = 0
        self.r = seed

    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.r = (a * self.r) % m
        return self.r

    def infinite_random_sequence(self):
        while True:
            self.steps += 1
            yield self.steps, random.random() * 100

    def random_sequence(self, length):
        return RandIter(self, length)


if __name__ == "__main__":
    random_number_generator = LCGRand(1)
    for rand in generator.random_sequence(10):
        print(rand)

    for i, rand in generator.infinite_random_sequence():
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break