class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        has1 = False
        for i, n in enumerate(nums):
            if n == 1:
                has1 = True
            if n <= 0 or n > len(nums):
                nums[i] = 1
        if not has1:
            return 1
        
        for i in range(len(nums)):
            value = abs(nums[i])
            if value == len(nums):
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return len(nums)
        return len(nums) + 1
        
            