class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = dict()
        for c in s:
            if c in m.keys():
                m[c] += 1
            else:
                m[c] = 0
        n = dict()
        for c in t:
            if c in n.keys():
                n[c] += 1
            else:
                n[c] = 0
        
        return m == n