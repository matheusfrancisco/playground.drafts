"""
Min Max Stack Construction
write a min max stack class for a min max stack. The class should support:
    - pushing and popping values on and off the stack
    - peeking at the value at the top the stack
    - getting both the minimum and the maximum values in the stack at any given 
    point time.

All class methos when cosidered independently, should run in constant time and
with constant space.
"""


class MinMaxStack:

    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        """
          O(1) Time
          O(1) Space
        """
        return self.stack[len(self.stack) - 1]

    def pop(self):
        """
          O(1) Time
          O(1) Space
        """
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        """
          O(1) Time
          O(1) Space
        """
        new = {"min": number, "max": number}
        if len(self.minMaxStack):
            last_min_max = self.minMaxStack[len(self.minMaxStack) - 1]
            new['min'] = min(last_min_max['min'], number)
            new['max'] = max(last_min_max['max'], number)
        self.minMaxStack.append(new)
        self.stack.append(number)

    def getMin(self):
        """
          O(1) Time
          O(1) Space
        """
        return self.minMaxStack[len(self.minMaxStack) - 1]['min']

    def getMax(self):
        """
          O(1) Time
          O(1) Space
        """
        return self.minMaxStack[len(self.minMaxStack) - 1]['max']


def test_min_max_stack():
    s = MinMaxStack()
    s.push(5)
    assert 5 == s.getMin()
    assert 5 == s.getMax()
    assert 5 == s.peek()
    s.push(7)
    assert 5 == s.getMin()
    assert 7 == s.getMax()
    assert 7 == s.peek()
    s.push(2)
    assert 2 == s.getMin()
    assert 7 == s.getMax()
    assert 2 == s.peek()
    v = s.pop()
    assert v == 2
    assert 5 == s.getMin()
    assert 7 == s.getMax()
    assert 7 == s.peek()
    v = s.pop()
    assert v == 7
    assert 5 == s.getMin()
    assert 5 == s.getMax()
    assert 5 == s.peek()
