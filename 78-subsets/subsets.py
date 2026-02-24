class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def dfs(i):
            if i > len(nums) - 1:
                return
            for subset in res.copy():
                res.append(subset + [nums[i]])
            dfs(i + 1)
        dfs(0)
        return res