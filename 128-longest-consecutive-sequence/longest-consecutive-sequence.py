class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        res = 0
        for n in m:
            if n - 1 not in m:
                cur = n
                cur_count = 1
                while cur + 1 in m:
                    cur += 1
                    cur_count += 1
                res = max(res, cur_count)
        
        return res
            