class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        cur = 0
        res = 0
        for i in range(len(cost)):
            cur = cur + gas[i] - cost[i]
            if cur < 0:
                res = i + 1
                cur = 0
        return res