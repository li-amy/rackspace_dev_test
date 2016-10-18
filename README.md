# rackspace_dev_test
Simple Distributed File Indexer
# Synopsis
The goal is to create a command-line indexer application that finds the top 10 words across a collection of documents.
So far, the logic for tokenizing blobs of text and returning the 10 most common unique words with their counts have been completed.
# Code Examples
`$ python tokenize.py pg34175.txt`

`$ python top_ten_words.py a a a A b c d`
# Installation
Unix:
Update the latest version of Python as instructed here: https://docs.python.org/3/using/unix.html. 
Next, clone or download this repository.

Windows:
Install and update the latest version of Python as instructed here: https://www.python.org/downloads/.
Next, download this repository.

# Tests
Install pytest.
`$ pip install -U pytest`

Execute pytest in the same directory as test_tokenize.py and test_top_ten_words.py files.
`$ pytest`

A report will then be generated.
