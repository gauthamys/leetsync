class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append([nums[i] for i in path])
                return
            for i in range(len(nums)):
                if i not in path:
                    backtrack(path + [i])
        backtrack([])
        return res
                