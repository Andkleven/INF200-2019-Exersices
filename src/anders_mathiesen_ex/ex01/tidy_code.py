# -*- coding: utf-8 -*-

from random import randint

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'


def get_guess_bigger_then_or_lik_1():
    number = 0
    while number < 1:
        number = input('Your guess bigger then or lik 1: ')
        try:
            number = int(number)
        except ValueError:
            print('Enter a number')
            number = 0
    return number


def get_random_number():
    return randint(1, 6) + randint(1, 6)


def check_if_guess_is_correct(random, one_guess):
    return random == one_guess


if __name__ == '__main__':

    right_guess = False
    number_of_guess = 3
    random_number = get_random_number()

    while not right_guess and number_of_guess > 0:
        guess = get_guess_bigger_then_or_lik_1()
        right_guess = check_if_guess_is_correct(random_number, guess)

        if not right_guess:
            print('Wrong, try again!')
            number_of_guess -= 1

    if number_of_guess > 0:
        print('You won {} points.'.format(number_of_guess))
    else:
        print('You lost. Correct answer: {}.'.format(random_number))
