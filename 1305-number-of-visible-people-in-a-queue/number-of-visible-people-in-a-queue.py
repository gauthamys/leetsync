class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stk = []
        n = len(heights)
        res = [0] * n
        
        for i in range(n):
            cur = heights[i]
            while stk and heights[stk[-1]] <= cur:
                res[stk.pop()] += 1
            if stk:
                res[stk[-1]] += 1
            stk.append(i)
       
        return res


