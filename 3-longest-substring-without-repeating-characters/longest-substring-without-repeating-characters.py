class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        res = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in m:
                new_l = m[s[r]] + 1
                while l < new_l:
                    del m[s[l]]
                    l += 1
            m[s[r]] = r
            res = max(res, (r - l + 1))
            r += 1
        return res
    
    # a b c a b c b b
    # l
    #       r