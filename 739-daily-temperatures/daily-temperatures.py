class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stk = [] # idx, temp
        for i, t in enumerate(temperatures):
            while stk and stk[-1][1] < t:
                idx = stk.pop()[0]
                answers[idx] = (i - idx)
            stk.append((i, t))
        return answers
