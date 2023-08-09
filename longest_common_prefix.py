from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        s = ""

        for letters in zip(*strs):
            if len(set(letters)) == 1:
                s += letters[0]
            else:
                break

        return s

    def longestCommonPrefix2(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans

print(Solution().longestCommonPrefix2(["flower","fire","flight"]))