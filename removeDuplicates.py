
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        for idx, n in enumerate(nums):
            i = idx + 1

            while len(nums) > i and nums[i] == n:
                if nums[i] == n:
                    nums.pop(i)

        return len(nums)

assert Solution().removeDuplicates([1,1,2]) == 2
assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
assert Solution().removeDuplicates([1,1]) == 1