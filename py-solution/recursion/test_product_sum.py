

def product_sum(array, multiplier = 1):
    s = 0
    for element in array:
        if type(element) is list:
            s += product_sum(element, multiplier + 1)
        else:
            s += element
    return s * multiplier


def test_product_sum():
    assert 12 == product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
