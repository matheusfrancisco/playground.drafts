import re

def reverse_words(sentence):
    # remove leading, trailing and multiple spaces
    sentence = re.sub(' +', ' ', sentence.strip())

    sentence = list(sentence)
    str_len = len(sentence)
    #  To reverse all words in the string, we will first reverse
    #  the entire string.
    str_rev(sentence, 0, str_len - 1)

    start = 0
    end = 0

    while True:
        # Find the start index of each word by detecting spaces.
        while start < len(sentence) and sentence[start] == ' ':
            start += 1

        if start == str_len:
            break

        # Find the end index of the word.
        end = start + 1
        while end < str_len and sentence[end] != ' ':
            end += 1

        # Let's call our helper function to reverse the word in-place.
        str_rev(sentence, start, end - 1)
        start = end

    return ''.join(sentence)


def str_rev(_str, start_rev, end_rev):
    # Starting from the two ends of the list, and moving
    # in towards the centre of the string, swap the characters
    while start_rev < end_rev:
        temp = _str[start_rev]          # temp store for swapping
        _str[start_rev] = _str[end_rev]  # swap step 1
        _str[end_rev] = temp            # swap step 2

        start_rev += 1                  # Move forwards towards the middle
        end_rev -= 1
