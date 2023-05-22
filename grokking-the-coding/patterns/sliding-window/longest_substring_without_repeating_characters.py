"""

Statement#
Given a string, input_string find the longest substring without repeating characters,
and return the length of that longest substring.

"""
def find_longest_substring(input_string):
    # Check the length of input_string
    if len(input_string) == 0:
        return 0

    n = len(input_string)
    st_curr, longest, len_curr, start = 0, 0, 0, 0

    last_seen_at = {}

    # Traverse input_string to find the longest substring
    # without repeating characters.
    for index, val in enumerate(input_string):
        # If the current element is not present in the hash map,
        # then store it in the hash map with the current index as the value.
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            # If the current element is present in the hash map,
            # it means that this element may have appeared before.
            # Check if the current element occurs before or after `st_curr`.
            print(last_seen_at, last_seen_at[val], val, st_curr)
            if last_seen_at[val] >= st_curr:
                len_curr = index - st_curr
                if longest < len_curr:
                    longest = len_curr
                    start = st_curr
                st_curr = last_seen_at[val] + 1

            # Update the last occurence of
            # the element in the hash map
            last_seen_at[val] = index

    index += 1
    # Update the longest substring's
    # length and starting index.
    if longest < index - st_curr:
        start = st_curr
        longest = n - st_curr

    return longest


assert find_longest_substring("abcabcbb") == 3
