import string


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed_string = reversed(s)

        for c in reversed_string:
            if c not in string.whitespace:
                break

        length = 1
        for c in reversed_string:
            if c not in string.whitespace:
                length += 1
            else:
                break

        return length

assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6