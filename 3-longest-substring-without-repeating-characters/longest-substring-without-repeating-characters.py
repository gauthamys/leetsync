class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l, r = 0, 0
        res = 0
        
        while r < len(s):
            if s[r] not in m:
                m[s[r]] = r
                r += 1
            else:
                new_l = m[s[r]] + 1
                for _ in range(l, new_l):
                    del m[s[l]]
                    l += 1
            res = max(res, (r - l))
        
        return res
    
    # a b c a b c b b
    #               l
    #               r