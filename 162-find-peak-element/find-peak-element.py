class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')

            if nums[mid] > left and nums[mid] > right: # peak
                return mid
            
            if nums[mid] > left: # left slope
                l = mid + 1
            
            else: # right slope
                r = mid - 1
        
        return l
    
    # 3 2 1
    # l r
    # m
