class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        def backtrack(idx):
            if idx > len(nums) - 1:
                return
            for subset in subsets[:]:
                subsets.append(subset + [nums[idx]])
            backtrack(idx + 1)

        backtrack(0)
        return subsets