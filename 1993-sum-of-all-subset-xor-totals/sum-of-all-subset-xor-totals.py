class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        cur = []
        def backtrack(idx):
            if idx == len(nums):
                if not cur:
                    res.append(0)
                else:
                    start = cur[0]
                    for i in range(1, len(cur)):
                        start ^= cur[i]
                    res.append(start)
                return
            backtrack(idx + 1)
            cur.append(nums[idx])
            backtrack(idx + 1)
            cur.pop()
        
        backtrack(0)
        return sum(res)