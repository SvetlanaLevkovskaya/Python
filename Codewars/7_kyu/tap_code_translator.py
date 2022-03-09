def tap_code_translation(text):
    letters = {'a': 0, 'b': 1, 'c': 2, 'k': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'l': 10, 'm': 11,
             'n': 12, 'o': 13, 'p': 14, 'q': 15, 'r': 16, 's': 17, 't': 18, 'u': 19, 'v': 20, 'w': 21, 'x': 22, 'y': 23,
             'z': 24}
    return ' '.join([int(letters[letter.lower()] / 5 + 1) * '.' + ' ' + (letters[letter.lower()] % 5 + 1)
                     * '.' for letter in text])


print(tap_code_translation("breaks"))


def tap_code_translation(text):
    dots = {'a': '. .', 'b': '. ..', 'c': '. ...', 'd': '. ....', 'e': '. .....', 'f': '.. .', 'g': '.. ..',
            'h': '.. ...', 'i': '.. ....', 'j': '.. .....', 'k': '. ...', 'l': '... .', 'm': '... ..', 'n': '... ...',
            'o': '... ....', 'p': '... .....', 'q': '.... .', 'r': '.... ..', 's': '.... ...', 't': '.... ....',
            'u': '.... .....', 'v': '..... .', 'w': '..... ..', 'x': '..... ...', 'y': '..... ....', 'z': '..... .....'}
    return ' '.join([dots[i] for i in text])


print(tap_code_translation("breaks"))
