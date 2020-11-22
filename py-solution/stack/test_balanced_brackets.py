"""
  Write a function that takes in a string made up of brackets
  ([{  )]} and other optinal characters. The function
  should return a boolean representing whether the string is balanced with
  regards to brackets.

  A string is said to be balanced if it has as many opening brackets of
  certion type it has closing brackets of that type and if no bracket is 
  unmatched .
  Note that an opening bracket can't match a corresponding closing bracket 
  that comes before it, and similarly, a closing bracket can't match a 
  corresponding openning bracket that comes after it. 
  Also, brackets can't overlap each other as in [(])
"""


def balanced_brackets(string):
    """
      Time O(n)
      Space O(n)
    """
    oppening_bracket = "([{"
    closing_brackets = "}])"
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char_bracket in string:
        if char_bracket in oppening_bracket:
            stack.append(char_bracket)
        elif char_bracket in closing_brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matching_brackets[char_bracket]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def balanced_brackets_(string):
    """ Time O(n)
        Space O(n)
    """
    brackets_to_add = "([{"
    brackets_to_remove = "}])"
    hash_brackets = {")": "(", "]": "[", "}": "{"}
    balanced_brackets = []

    for bracket in string:
        if bracket in brackets_to_add:
            balanced_brackets.append(bracket)
        elif bracket in brackets_to_remove:
            if len(balanced_brackets) == 0:
                return False
            poped_backet = hash_brackets.get(bracket)
            value_poped = balanced_brackets.pop()
            if value_poped != poped_backet:
                return False
    if(len(balanced_brackets)) > 0:
        return False
    return True


def test_balaced_brackets():
    assert balanced_brackets("()(){}[]{}") is True
    assert balanced_brackets(")(){}[]{}") is False
    assert balanced_brackets("(){[]{}") is False
    assert balanced_brackets("(){") is False
    assert balanced_brackets_("()(){}[]{}") is True
    assert balanced_brackets_(")(){}[]{}") is False
    assert balanced_brackets_("(){[]{}") is False
    assert balanced_brackets_("(){") is False
