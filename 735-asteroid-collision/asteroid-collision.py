class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            if not stk or stk[-1] / abs(stk[-1]) == a / abs(a):
                stk.append(a)
            else:
                explode = False
                new = a
                while stk and new < 0 and stk[-1] > 0:
                    top = stk.pop()
                    if top + a == 0:
                        explode = True
                        break
                    new = top if abs(top) > abs(new) else new
                if not explode:
                    stk.append(new)
        return stk
                
