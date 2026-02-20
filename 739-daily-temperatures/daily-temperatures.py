class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            #print(stk)
            if not stk or stk[-1][0] >= t:
                stk.append((t, i))
            elif t > stk[-1][0]:
                while stk and stk[-1][0] < t:
                    curT, curI = stk.pop()
                    res[curI] = i - curI
                stk.append((t, i))
        return res