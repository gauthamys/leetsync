class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(start):
            res.append(cur[:])
            if start >= len(nums):
                return
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1)
                cur.pop()
        backtrack(0)
        return res