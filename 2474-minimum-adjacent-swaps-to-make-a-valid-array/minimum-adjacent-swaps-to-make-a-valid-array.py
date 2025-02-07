class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the smallest and largest values in the array.
        min_val = min(nums)
        max_val = max(nums)
        
        # Get the index of the first occurrence of the smallest element.
        pos_min = nums.index(min_val)
        
        # Get the index of the last occurrence of the largest element.
        # One way to do this is to reverse the list and find the index, then convert it.
        pos_max = n - 1 - nums[::-1].index(max_val)
        
        # Compute the number of swaps:
        swaps = pos_min + ((n - 1) - pos_max)
        
        # If the smallest element is to the right of the largest element,
        # subtract 1 to account for the overlap.
        if pos_min > pos_max:
            swaps -= 1
            
        return swaps
