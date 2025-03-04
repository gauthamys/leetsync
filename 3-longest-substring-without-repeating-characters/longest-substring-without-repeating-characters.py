class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        m = {}
        while r < len(s):
            if s[r] not in m:
                m[s[r]] = r
                r += 1
            else:
                new_l = m[s[r]] + 1
                for i in range(l, m[s[r]] + 1):
                    del m[s[i]]
                l = new_l
            res = max(res, (r - l))
        return res