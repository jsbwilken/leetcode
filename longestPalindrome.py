class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = 0
        palindrome_idx = 0

        mat = [[0 for _ in range(__ + 1)] for __ in range(len(s) + 1)]

        for i in range(len(s)):
            for n in range(i + 1):
                if s[i] == s[-1-n]:
                    if i - 1 >= 0 and n - 1 >= 0:
                        mat[i][n] = 1 + mat[i - 1][n - 1]
                    else:
                        mat[i][n] = 1

                    if mat[i][n] > longest_palindrome:
                        longest_palindrome = mat[i][n]
                        palindrome_idx = i

        palindrome = ""
        while longest_palindrome > 0:
            palindrome += s[palindrome_idx]
            palindrome_idx -= 1
            longest_palindrome -= 1

        return palindrome


assert Solution().longestPalindrome("ccd") in ["cc"]
assert Solution().longestPalindrome("racecar") in ["racecar"]
assert Solution().longestPalindrome("babad") in ["bab", "aba"]
assert Solution().longestPalindrome("cbbd") in ["bb"]
