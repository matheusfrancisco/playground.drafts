"""
time O(n)
space O(n)
Ceasar Cipher Encryptor

Given a non-empty string of lowercase letters and a non-negative integer representing a key,
write a function that returns a new string obtained by shifting every letter in the input
string by k positions in the alphabet, where k is the key

Note that letters should "wrap" around the alphabet; in other words, the letter z shifed by one returns
the letter a.

"""


def get_new_letter(old_letter, key):
    new_letter_code = ord(old_letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122) # noqa


def caesar_cipher_encryptor(string, key):
    new_letters = []
    key = key % 26
    for letter in string:
        new_letters.append(get_new_letter(letter, key))
    return "".join(new_letters)


def test_caesar_cipher():
    assert "zab" == caesar_cipher_encryptor("xyz", 2)
