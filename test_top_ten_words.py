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

def test_answer():
    # Testing empty list.
    assert top_ten_words([]) == []
    # Testing a list containing a single token.
    assert top_ten_words(['A']) == [('A', 1)]
    # Testing a list containing two tokens of the same count.
    assert top_ten_words(['aa', 'ab']) == [('aa', 1), ('ab', 1)]
    # Testing a list containing 10 unique tokens
    assert top_ten_words(['a', 'a', 'a' , 'a', 'a', 
        'A', 'A', 'A', 'A', 'A', 'aa', 'aa', 'aa', 'aa', 
        'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c',
        '0', '0', '0', 'B', 'B', 'B', '9', '9', '9',
        'zZ9', '99'] == [('a', 5), ('A', 5), ('aa', 4), ('b', 4), ('c', 4), 
        ('0', 3), ('B', 3), ('9', 3), ('zZ9', 1), ('99', 1)])
    # Testing a list containing more than 10 unique tokens
    assert top_ten_words(['a', 'a', 'a' , 'a', 'a', 
        'A', 'A', 'A', 'A', 'A', 'aa', 'aa', 'aa', 'aa', 
        'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c',
        '0', '0', '0', 'B', 'B', 'B', '9', '9', '9',
        'zZ9', '99', 'd0f8'] == [('a', 5), ('A', 5), ('aa', 4), ('b', 4), ('c', 4), 
        ('0', 3), ('B', 3), ('9', 3), ('zZ9', 1), ('99', 1)])