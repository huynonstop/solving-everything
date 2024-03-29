from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return max_area(height)


def max_area(height):
    l = 0
    r = len(height) - 1
    m = 0
    while l < r:
        m = max(m, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return m


max_area(
    [1, 8, 6, 2, 5, 4, 8, 3, 7])
