class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        def backtrack(pathLen):
            if pathLen == n:
                res.append(cur[:])
                return
            for i in range(n):
                if nums[i] not in cur[:]:
                    cur.append(nums[i])
                    backtrack(pathLen + 1)
                    cur.pop()
        backtrack(0)
        return res