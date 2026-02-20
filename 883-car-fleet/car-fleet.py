class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = sorted(zip(position, speed), key=lambda x: -x[0])
        stk = []
        for p, s in times:
            t = (target - p) / s
            if stk and t <= stk[-1]:
                continue
            else:
                stk.append(t)
        return len(stk)