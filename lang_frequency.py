import sys
import os
import re
import collections
import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        sys.exit('File does not exists: {0}'.format(filepath))
    with open(filepath, 'r') as file_handler:
        return file_handler.read() 


def make_words_counter(text):
    words_counter = collections.Counter()
    words = [word.lower() for word in re.split('\W+', text) if word]
    words_counter.update(words)
    return words_counter


def get_most_frequent_words(words_counter, count):
    return [x[0] for x in words_counter.most_common(count)]


def print_freq_words(word_list):
    pprint.pprint(word_list)


if __name__ == '__main__':
    count_required_sys_args = 2
    count_freq_words = 10
    if len(sys.argv) != count_required_sys_args:
        sys.exit('Usage: python lang_frequency.py <path to file>')
    text_in_file = load_data(sys.argv[1])
    words_counter = make_words_counter(text_in_file)
    print_freq_words(get_most_frequent_words(words_counter, count_freq_words))
