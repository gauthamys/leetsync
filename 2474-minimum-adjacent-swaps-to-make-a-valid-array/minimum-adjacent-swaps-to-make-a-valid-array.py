class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        min_val = min(nums)
        max_val = max(nums)
        
        pos_min = nums.index(min_val)
        
        pos_max = n - 1 - nums[::-1].index(max_val)
        
        swaps = pos_min + ((n - 1) - pos_max)
        
        if pos_min > pos_max:
            swaps -= 1
            
        return swaps
