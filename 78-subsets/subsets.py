class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def backtrack(idx):
            if idx >= len(nums):
                return 
            for subset in res[:]:
                res.append(subset + [nums[idx]])
            backtrack(idx + 1)
        backtrack(0)
        return res