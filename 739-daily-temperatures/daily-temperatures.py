class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] # pair (t, i)
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            days = 0
            while stk and stk[-1][0] < temperatures[i]:
                t, index = stk.pop()
                res[index] = i - index
            stk.append((temperatures[i], i))
        return res