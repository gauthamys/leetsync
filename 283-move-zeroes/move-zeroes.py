class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        stk = []
        for n in nums:
            if n != 0:
                res.append(n)
            else:
                stk.append(n)
        
        res = res + stk
        for i in range(len(nums)):
            nums[i] = res[i]
        
        
