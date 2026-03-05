class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0] * len(nums)
        pre = 0
        counts = {0: 1}
        res = 0

        for i in range(len(nums)):
            pre += nums[i]
            prefix[i] = pre
            if pre - goal in counts:
                res += counts[pre - goal]
            counts[pre] = counts.get(pre, 0) + 1
        
        return res
        