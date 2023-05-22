class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            "(": ")", "{": "}", "[": "]"
        }
        stack = []
        for bracket in s:
            if bracket in close:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                char = stack.pop()
                if close.get(char) != bracket:
                    return False
        return len(stack) == 0
