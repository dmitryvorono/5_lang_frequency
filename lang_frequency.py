import sys
import os
import re
import collections
import pprint


def load_data(filepath):
    words_counter = collections.Counter()
    if not os.path.exists(filepath):
        sys.exit('File does not exists: {0}'.format(filepath))
    for line in open(filepath, 'r'):
        words = [word.lower() for word in re.split('\W+', line) if word]
        words_counter.update(words)
    return words_counter


def get_most_frequent_words(words_counter, count):
    return [x[0] for x in words_counter.most_common(count)]


def print_freq_words(word_list):
    pprint.pprint(word_list)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: python lang_frequency.py <path to file>')
    file_name = sys.argv[1]
    words_counter = load_data(file_name)
    print_freq_words(get_most_frequent_words(words_counter, 10))
