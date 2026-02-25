class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def backtrack():
            if len(path) == len(nums):
                if [nums[i] for i in path[:]] not in res:
                    res.append([nums[i] for i in path[:]])
                return
            for i in range(len(nums)):
                if i not in path:
                    path.append(i)
                    backtrack()
                    path.pop()
        backtrack()
        return res