class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        res = []
        for i, a in enumerate(asteroids):
            if a < 0:
                while stk and stk[-1] < -a:
                    stk.pop()
                if stk and stk[-1] == -a:
                    stk.pop()
                    continue
                if not stk:
                    res.append(a)
                continue
            stk.append(a)
        return res + stk