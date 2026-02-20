class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        res = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            if (cur - k) in counts:
                res += counts[cur - k]
            counts[cur] = counts.get(cur, 0) + 1
        return res