class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        lookup = {}
        l, r = 0, 0
        while r < n:
            if s[r] in lookup:
                l = max(lookup[s[r]], l)
            
            res = max(res, r - l + 1)
            lookup[s[r]] = r + 1
            r += 1
        
        return res
                