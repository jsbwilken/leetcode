from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int, start: int = None, end: int = None) -> int:

        if start is None:
            start = 0

        if end is None:
            end = len(nums)

        center = ((end + start) // 2)

        if nums[center] > target:
            if start == center:
                return start
            return self.searchInsert(nums, target, start, center)
        elif nums[center] < target:
            if start == center:
                return start + 1
            return self.searchInsert(nums, target, center, end)
        else:
            return center


assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert([1,3,5,6], 2) == 1
assert Solution().searchInsert([1,3,5,6], 7) == 4