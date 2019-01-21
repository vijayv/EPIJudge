from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    mag_dict = Counter(magazine_text)
    for c in letter_text:
        if c not in mag_dict:
            return False
        mag_dict[c] -= 1
        if mag_dict[c] < 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
