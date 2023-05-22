
def is_valid_subsquence(array, seq):
    arr_index = 0
    seq_index = 0
    while arr_index < len(array) and seq_index < len(seq):
        if array[arr_index] == seq[seq_index]:
            seq_index += 1
        arr_index += 1
    return seq_index == len(seq)


def test_subsquence():
    assert is_valid_subsquence(
        [5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]
    ) is True
