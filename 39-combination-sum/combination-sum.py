class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(start, curSum):
            if curSum == target:
                res.append(cur[:])
                return
            if curSum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(i, curSum + candidates[i])
                cur.pop()
        
        backtrack(0, 0)
        return res
            
            