from solutions import (
    is_unique,
    is_unique_with_counter,
    is_string_permutation,
    escape_spaces_urlfy,
    string_compression,
)


def test_string_has_all_unique_characters_return_true():
    assert is_unique("Matheus") is True


def test_string_has_all_unique_characters_return_false():
    assert is_unique("maaatheus") is False


def test_counter_string_has_all_unique_characters_return_true():
    assert is_unique_with_counter("Matheus") is True


def test_counter_string_has_all_unique_characters_return_false():
    assert is_unique_with_counter("maaatheus") is False


def test_should_return_true_if_string2_is_premutation_string1():
    assert is_string_permutation("matheus", "suehtam") is True


def test_should_return_false_if_string2_is_premutation_string1():
    assert is_string_permutation("matheus", "sam") is False


def test_should_substitue_spaces():
    expected = "Hi%20my%20name%20is%20Xico"
    assert escape_spaces_urlfy(" Hi my name is Xico ") == expected


def test_string_compression_function():
    assert string_compression("aabbbccccceeeeeee") == "a2b3c5e7"
    assert string_compression("aaa") == "a3"
    assert string_compression("aa") == "a2"
    assert string_compression("a") == "a1"
    assert string_compression("") == ""
    assert string_compression("aaabbc") == "a3b2c1"
