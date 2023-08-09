import math
from typing import Optional

# [1,2,3,4,5]
# left = 0
# right = 4
# center = 2
# step = 2

# [1,2,3]
# left = 0
# right = 2
# center = 1
# step = 1






class Solution:

    def strStr(self, haystack: str, needle: str, left: int = None, right: int = None) -> int:

        if left is None:
            left = 0

        if right is None:
            right = len(haystack) - len(needle)

        step = (right - left) // 2

        if step == 0:
            if haystack[left:left+len(needle)] == needle:
                return left
            elif haystack[right:right+len(needle)] == needle:
                return right
            else:
                return -1

        left_result = self.strStr(haystack, needle, left, right - step)
        if left_result != -1:
            return left_result

        return self.strStr(haystack, needle, left + step, right)


assert Solution().strStr("sadbutsad", "sad") == 0
assert Solution().strStr("leetcode", "leeto") == -1
assert Solution().strStr("hello", "ll") == 2

