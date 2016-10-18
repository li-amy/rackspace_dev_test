#!/usr/bin/python
import sys

def top_ten_words(word_list):
    """Returns the top 10 words and their counts."""
    word_dict = {}
    for word in word_list:
        # Add the word and its count into the dictionary if it's unique.
        if word not in word_dict.keys():
            word_count = word_list.count(word)
            word_dict[word] = word_count
    # Sort the dictionary by the count value in descending order. Take the first 10 items.
    top_ten = sorted(word_dict.iteritems(), key = lambda w: w[1], reverse = True)[:10]
    return top_ten
   
if __name__ == '__main__':
    top_ten = top_ten_words(sys.argv[1:])
    print top_ten
else:
    print 'top_ten_words has been imported.'