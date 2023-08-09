from typing import Literal


class Solution:

    def getSingleValue(self, s: Literal["I", "V", "X", "L", "C", "D", "M"]) -> int:
        match s:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
    def romanToInt(self, s: str) -> int:
        letters = list(s)
        value = 0

        while len(letters):
            l = letters.pop()
            v = self.getSingleValue(l)

            if len(letters):
                v_next = self.getSingleValue(letters[-1])

                if v_next < v:
                    value += v - v_next
                    letters.pop()
                else:
                    value += v
            else:
                value += v

        return value


assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("LVIII") == 58
assert Solution().romanToInt("MCMXCIV") == 1994