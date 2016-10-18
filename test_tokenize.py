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

def test_answer():
    # Testing empty string
    assert tokenize("") == []
    # Testing a single alphanumeric character.
    assert tokenize("a") == ['a']
    # Testing a string of alphanumeric characters with no delimiters.
    assert tokenize("AA") == ['AA']
    # Testing a string of alphanumeric characters with delimiters.
    assert tokenize("0 ! a-d0f8") == ['0', 'a', 'd0f8']