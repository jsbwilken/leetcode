class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        char_seen = {}
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char not in char_seen:
                longest_substring = max(longest_substring, right - left + 1)
            else:
                if char_seen[char] >= left:
                    left = char_seen[char] + 1
                else:
                    longest_substring = max(longest_substring, right - left + 1)

            char_seen[char] = right

        return longest_substring

assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("cdd") == 2
assert Solution().lengthOfLongestSubstring("dvdf") == 3
assert Solution().lengthOfLongestSubstring(" ") == 1
assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5
