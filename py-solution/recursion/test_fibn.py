

def fib(n):
    """
      O(2^n): time
      O(n): space
    """
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return fib(n-1) + fib(n-2)


def get_nth_fib(n):
    return fib(n)


def test_get_n_fib():
    assert 5 == get_nth_fib(6)
