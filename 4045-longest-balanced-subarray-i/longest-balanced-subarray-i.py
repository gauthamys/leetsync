class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            evens = set()
            odds = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 1:
                    odds.add(nums[j])
                else:
                    evens.add(nums[j])
                
                if len(evens) == len(odds):
                    res = max(res, (j - i + 1))
        return res