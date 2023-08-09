from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    diff_map = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in diff_map:
            return [idx, diff_map[diff]]
        else:
            diff_map[num] = idx


twoSum([2,7,11,15],9)