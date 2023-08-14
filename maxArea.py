from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        area = min(height[left], height[right]) * (right - left)

        while left != right:
            while height[left] <= height[right] and left < right:
                left += 1
                current_area = min(height[left], height[right]) * (right - left)
                if current_area > area:
                    area = current_area

            while height[right] < height[left] and right > left:
                right -= 1
                current_area = min(height[left], height[right]) * (right - left)
                if current_area > area:
                    area = current_area

        return area

assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([1,1]) == 1
