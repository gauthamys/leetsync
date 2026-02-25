class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        res_r, res_l = float('inf'), 0
        l, r = 0, 0
        have = {}

        def check():
            for ch in need:
                if ch not in have or have[ch] < need[ch]:
                    return False
            return True

        while r < len(s):
            if s[r] in need:
                have[s[r]] = have.get(s[r], 0) + 1
            
            if check():
                while check():
                    if (r - l) < (res_r - res_l):
                        res_r, res_l = r, l
                    if s[l] in need:
                        have[s[l]] -= 1
                    l += 1
            r += 1
        
        return s[res_l:res_r+1] if res_r != float('inf') else ""