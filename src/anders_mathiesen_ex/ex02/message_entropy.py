from math import log2


def letter_freq(txt):
    frequencies = {}
    for symbol in list(txt):
        symbol = symbol.lower()
        if symbol in frequencies:
            frequencies[symbol] += 1
        else:
            frequencies[symbol] = 1

    return frequencies


def entropy(message):
    n = len(message)
    frequencies = letter_freq(message)
    h = 0
    for value in frequencies.values():
        p_i = value/n
        h -= p_i*log2(p_i)
    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
