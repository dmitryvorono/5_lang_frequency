import sys
import os
import re
import collections


def load_data(filepath):
    words_counter = collections.Counter()
    if not os.path.exists(filepath):
        return None
    for line in open(filepath, 'r'):
        words = [word.lower() for word in re.split('\W+', line) if word]
        words_counter.update(words)
    return words_counter


def get_most_frequent_words(words_counter):
    return [x[0] for x in words_counter.most_common(10)]


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Usage: python lang_frequency.py <path to file>')
        sys.exit(2)
    words_counter = load_data(file_name)
    print(get_most_frequent_words(words_counter))
