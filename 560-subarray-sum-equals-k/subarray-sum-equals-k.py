class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0: 1}
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            if (prefix - k) in pre:
                res += pre[prefix - k]
            if prefix in pre:
                pre[prefix] += 1
            else:
                pre[prefix] = 1
        return res