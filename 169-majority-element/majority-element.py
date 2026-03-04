class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
            if counts[n] > majority:
                return n