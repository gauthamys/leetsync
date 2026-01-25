class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in m:
                new_l = m[s[r]] + 1
                for i in range(l, new_l):
                    del m[s[i]]
                l = new_l
            else:
                res = max(res, (r - l + 1))
                m[s[r]] = r
                r += 1
        
        return res