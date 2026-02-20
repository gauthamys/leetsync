class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f = len(nums) / 3
        res = set()
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            if n not in counts:
                counts[n] = 1
            if counts[n] > f:
                res.add(n)
        return list(res)
            