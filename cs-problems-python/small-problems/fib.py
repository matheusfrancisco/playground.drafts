from functools import lru_cache
from typing import Dict
import unittest
import pytest
"""
The fibonacci sequence
0, 1, 1, 2, 3, 5, 8, 13, 21...

fib(n) = fib(n-1) + fib(n-2)
"""


class TestFib(unittest.TestCase):
    def test_fib_recursion_max(self):
        with self.assertRaises(RecursionError) as context:
            fib(5)


def test_fib_recursion_error():
    with pytest.raises(RecursionError):
        assert fib(5)


def test_fib_with_base_case_return_1():
    assert fib_base_case(1) == 1



def test_fib_base_case_should_return_21_n_8():
    assert fib_base_case(8) == 21


def fib(n: int) -> int:
    """ this code have a problem
    RecursionError: maximum recursion depth exceeded """
    return fib(n-1)+fib(n-2)


def fib_base_case(n: int) -> int:
    if n < 2:
        return n
    return fib_base_case(n-2) + fib_base_case(n-1)


"""
fib(4) -> fib(3), fib(2)
fib(3) -> fib(2), fib(1)
fib(2) -> fib(1), fib(0)
fib(2) -> fib(1), fib(0)
fib(1) -> 1
fib(1) -> 1
fib(1) -> 1
fib(0) -> 0
fib(0) -> 0
"""


def test_fib_with_memo_n_1():
    assert fib_with_memo(1) == 1


def test_fib_with_memo_should_return_21_n_8():
    assert fib_with_memo(8) == 21


memo: Dict[int, int] = {0: 0, 1: 1}


def fib_with_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_with_memo(n-1)+fib_with_memo(n-2)
    return memo[n]


@lru_cache(maxsize=None)
def fib_with_lr_cache(n: int) -> int:
    if n < 2:
        return n
    return fib_with_lr_cache(n-2) + fib_with_lr_cache(n-1)


if __name__ == "__main__":
    unittest.main()
