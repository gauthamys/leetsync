class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {} # (right, diff): len
        res = 0
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                dp[(right, diff)] = dp.get((left, diff), 1) + 1
                res = max(res, dp[(right, diff)])
        return res