# -*- coding: utf-8 -*-


def letter_freq(txt):
    frequency = {}
    for symbol in list(txt):
        symbol = symbol.lower()
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1

    return frequency


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
