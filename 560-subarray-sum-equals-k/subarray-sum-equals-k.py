class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        cur = 0
        res = 0
        
        for i in range(len(nums)):
            cur += nums[i]
            rem = cur - k

            if rem in counts:
                res += counts[rem]
            
            counts[cur] = counts.get(cur, 0) + 1
        
        return res
        
