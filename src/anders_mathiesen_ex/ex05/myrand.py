# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'

import random


class RandIter:
    def __init__(self, random_number_generator, length):
        """
        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None
        self.is_iter = False

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.is_iter:
            raise RuntimeError
        self.is_iter = True
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.is_iter:
            raise RuntimeError
        if self.num_generated_numbers <= self.length:
            raise StopIteration
        self.num_generated_numbers += 1
        return self.generator


class LCGRand:
    def __init__(self, seed):
        """
        Initialise a linear congruence random number generator

        Arguments
        ---------
        seed : int
            The initial seed for the generator
        """
        self.steps = 0
        self.r = seed

    def rand(self):
        """
        Generate a single random number.

        Returns
        -------
        int
            A random integer
        """
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.r = (a * self.r) % m
        return self.r

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
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