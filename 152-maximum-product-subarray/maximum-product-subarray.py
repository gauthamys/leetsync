class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]
            tmp = max(cur, cur * max_so_far, cur * min_so_far)
            min_so_far = min(cur, cur * max_so_far, cur * min_so_far)
            max_so_far = tmp

            res = max(res, tmp)
        
        return res