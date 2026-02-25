class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    backtrack(path + [nums[i]])
        backtrack([])
        return res
                