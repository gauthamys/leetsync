class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {nums[0]: 1}
        prefix = nums[0]
        res = 0
        if nums[0] == k:
            res += 1
        for n in nums[1:]:
            if prefix + n == k:
                res += 1
            if (prefix + n - k) in pre:
                res += pre[prefix + n - k]
            if prefix + n in pre:
                pre[prefix + n] += 1
            else:
                pre[prefix + n] = 1
            prefix += n
        return res