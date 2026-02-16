class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        res = 0
        while l < r:
            left_max = max(height[l], left_max)
            right_max = max(height[r], right_max)
            res += (left_max - height[l]) + (right_max - height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res