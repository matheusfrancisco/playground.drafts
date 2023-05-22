"""
  You're given a string of length 12 or smaller, containing only digits.
  Write a function that returns all the possible IP addresses that can
  be created by inserting three . s in the string.

  An IP address is a sequence of four positive integers that are separated by .
  s, where each individual integer is within the range 0 - 255, inclusive

  An IP address isn't valid if any of the individual integers contains leading
  0 s, For example "192.168.0.1", is a valid IP address, but "192.168.00.1" and
  "192.168.0.01" aren't, because they contain "00" and "01", respectivley.
  Another example of a valid IP address is "99.1.1.10"; conversely, "991.1.1.0"
  isn't valid, because "991" is greater than 255.

  Your function should return the ip address in string format and in no
  particular order. If no valid IP addresses can be created from the string,
  your function should return an empty list.

  Note: check out our systems design fundamentls on systems express to
  learn more about  IP addresses!

"""


def valid_ip_addreses(string):
    """
      Time O(1)
      Space O(1)
    """
    valids_ips = []
    for i in range(1, min(len(string), 4)):
        current_ip_address_parts = ['', '', '', '']
        current_ip_address_parts[0] = string[:i]
        if not is_valid_part(current_ip_address_parts[0]):
            continue
        for j in range(i + 1, i + min(len(string) - i, 4)):
            current_ip_address_parts[1] = string[i:j]
            if not is_valid_part(current_ip_address_parts[1]):
                continue
            for k in range(j + 1, j + min(len(string) - j, 4)):
                current_ip_address_parts[2] = string[j:k]
                current_ip_address_parts[3] = string[k:]
                if is_valid_part(current_ip_address_parts[2]) and is_valid_part(current_ip_address_parts[3]): # noqa
                    valids_ips.append('.'.join(current_ip_address_parts))
    return valids_ips


def is_valid_part(string):
    string_as_int = int(string)
    if string_as_int > 255:
        return False
    return len(string) == len(str(string_as_int))  # check for leading 0


def test_ip_address():
    ip = "1921680"
    expected = [
        "1.9.216.80",
        "1.92.16.80",
        "1.92.168.0",
        "19.2.16.80",
        "19.2.168.0",
        "19.21.6.80",
        "19.21.68.0",
        "19.216.8.0",
        "192.1.6.80",
        "192.1.68.0",
        "192.16.8.0",
    ]
    assert valid_ip_addreses(ip) == expected
