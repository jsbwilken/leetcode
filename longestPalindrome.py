class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = -1
        palindrome = ""

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if (right - left + 1) > max_length:
                        palindrome = s[left:right+1]
                        max_length = right - left + 1

                    left -= 1
                    right += 1
                else:
                    break

            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if (right - left + 1) > max_length:
                        palindrome = s[left:right+1]
                        max_length = right - left + 1

                    left -= 1
                    right += 1
                else:
                    break

        return palindrome


assert Solution().longestPalindrome("ccc") in ["ccc"]
assert Solution().longestPalindrome("a") in ["a"]
assert Solution().longestPalindrome("ccd") in ["cc"]
assert Solution().longestPalindrome("racecar") in ["racecar"]
assert Solution().longestPalindrome("babad") in ["bab", "aba"]
assert Solution().longestPalindrome("cbbd") in ["bb"]
