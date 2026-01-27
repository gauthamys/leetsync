class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            if not stk or temperatures[i] <= stk[-1][0]:
                stk.append((temperatures[i], i))
            else:
                while stk and temperatures[i] > stk[-1][0]:
                    top = stk.pop()
                    ans[top[1]] = i - top[1]
                stk.append((temperatures[i], i))
        
        return ans

        