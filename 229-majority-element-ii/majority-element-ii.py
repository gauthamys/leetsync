class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f = len(nums) / 3
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        return [x[0] for x in filter(lambda x: x[1] > f, counts.items())]
            