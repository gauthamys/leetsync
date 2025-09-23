class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i + 1] + nums[i - 1] == nums[i] / 2:
                res += 1
        
        return res