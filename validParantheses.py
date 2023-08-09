
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        letters = list(s)

        if len(s) % 2 == 1:
            return False

        while len(letters):
            c = letters.pop(0)

            if c in "({[":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != "[":
                    return False

        return len(stack) == 0




assert Solution().isValid("()")
assert Solution().isValid("()[]{}")
assert not Solution().isValid("(]")