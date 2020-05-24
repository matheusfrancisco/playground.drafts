from solutions import is_unique, is_unique_with_counter, is_string_permutation


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
