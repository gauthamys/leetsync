class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        pre = 0
        counts = {0: 1}
        res = 0
        
        for i in range(len(nums)):
            pre += nums[i]
            prefix[i] = pre

            target = prefix[i] - k
            if target in counts:
                res += counts[target]
            
            counts[pre] = counts.get(pre, 0) + 1
        
        return res
        
