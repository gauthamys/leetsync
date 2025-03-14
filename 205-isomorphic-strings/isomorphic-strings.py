class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        seen = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            if s[i] not in m:
                if t[i] in seen:
                    return False
                m[s[i]] = t[i]
                seen.add(t[i])
        return True