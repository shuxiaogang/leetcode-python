from typing import List


class Solution:
    # 双指针
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height) - 1, 0
        while left != right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    # 中心扩散
    def maxArea1(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height)):
            min_pos = i
            for pos in range(0, i):
                if height[pos] >= height[i]:
                    min_pos = pos
                    break
            max_pos = i
            for pos in range(len(height) - 1, i, -1):
                if height[pos] >= height[i]:
                    max_pos = pos
                    break
            max_area = max(max_area, (max_pos - min_pos) * height[i])
        return max_area


print(Solution().maxArea([2,3,4,5,18,17,6]))
