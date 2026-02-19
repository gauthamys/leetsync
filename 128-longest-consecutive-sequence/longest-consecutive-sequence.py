class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if n - 1 not in s:
                cur = 1
                curNum = n
                while curNum + 1 in s:
                    curNum += 1
                    cur += 1
                res = max(res, cur)
        return res