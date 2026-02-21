class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = []
        m = {0: -1}
        pre = 0
        res = float('inf')
        for i, n in enumerate(nums):
            cur = float('inf')
            pre += n
            prefix.append(pre)
            m[pre] = i
            for j in range(pre - target, -1, -1):
                if j in m:
                    cur = i - m[j]
                    break
            res = min(res, cur)
        return 0 if res == float('inf') else res
            