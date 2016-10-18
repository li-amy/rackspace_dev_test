#!/usr/bin/python
import argparse
import sys

def tokenize(text):
    """Returns a list of words."""
    word_list = []
    curr_word = ''
    for char in text:
        # Check if character is a-z, A-Z, or 0-9.
        if char.isalnum():
            curr_word += char
        # Else, delimit word.
        else:
            if curr_word:
                word_list.append(curr_word)
                curr_word = ''
    # Including last word if it is a valid word.
    if curr_word: word_list.append(curr_word)
    return word_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tokenize blobs of text.', 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='+', default=sys.stdin, 
        help='Input at least 1 text file, else accepts standard input.')
    args = parser.parse_args()
    input_word_list = []
    for f in args.infile:
        text = f.read()
        file_word_list = tokenize(text)
        input_word_list.extend(file_word_list)
    print input_word_list
else:
    print 'tokenize has been imported.'