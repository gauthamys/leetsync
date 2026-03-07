class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [] # time reached
        for p, s in sorted(zip(position, speed), key=lambda x: -x[0]):
            t = (target - p) / s
            if stk and stk[-1] >= t:
                continue
            stk.append(t)
        return len(stk)