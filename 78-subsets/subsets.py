class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            for subset in subsets[:]:
                subsets.append(subset + [num])
        
        return subsets