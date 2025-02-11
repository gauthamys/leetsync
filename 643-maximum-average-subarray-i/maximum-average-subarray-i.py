class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        for i in range(len(nums)):
            nums[i] /= k
        
        res = float('-inf')
        curSum = sum(nums[:k])
        res = max(res, curSum)
        l, r = 0, k
        while r < len(nums):
            print(l, r)
            res = max(res, curSum)
            curSum -= nums[l]
            curSum += nums[r]
            l += 1
            r += 1
        
        return max(res, curSum)
        
