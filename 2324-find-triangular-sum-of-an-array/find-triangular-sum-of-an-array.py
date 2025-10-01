class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        cur = nums
        while len(cur) > 1:
            new = []
            for i in range(len(cur) - 1):
                new.append((cur[i] + cur[i + 1]) % 10)
            cur = new

        return cur[0]