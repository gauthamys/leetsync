class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        pre = 0
        while r < len(nums):
            pre += nums[r]
            while pre >= target:
                res = min(res, r - l + 1)
                pre -= nums[l]
                l += 1
            r += 1
        return 0 if res == float('inf') else res
