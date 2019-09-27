def char_counts(textfilename):
    result_list = [0 for _ in range(256)]
    with open(textfilename, 'r', encoding='utf8') as fp:
        for line in fp.readlines():
            word_list = list(line)
            for word in word_list:
                character_code = ord(word)
                result_list[character_code] += 1
    return result_list


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
