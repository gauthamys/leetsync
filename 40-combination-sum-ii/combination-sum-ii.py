class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()
        
        def backtrack(start, curSum):
            if curSum == target:
                res.append(cur[:])
            
            if start >= len(candidates) or curSum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(i + 1, curSum + candidates[i])
                cur.pop()
        
        backtrack(0, 0)
        return res