def run_length_encoding(string):
    encoded_string_characters = []
    current_run_length = 1
    for i in range(1, len(string)):
        current_character = string[i]
        previous_character = string[i - 1]
        if current_character != previous_character or current_run_length == 9:
            encoded_string_characters.append(str(current_run_length))
            encoded_string_characters.append(previous_character)
            current_run_length = 0
        current_run_length += 1
    encoded_string_characters.append(str(current_run_length))
    encoded_string_characters.append(string[len(string) - 1])
    return "".join(encoded_string_characters)


def test_run_length_encoding():
    string = "AAAAAAAAAAAABBBCCCDD"
    assert run_length_encoding(string) == "9A3A3B3C2D"
