class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = {}
        
        for s in strings:
            key = ''
            for i in range(1, len(s)):
                key += str((ord(s[i]) - ord(s[i - 1])) % 26 + ord('a'))
            m[key] = m.get(key, [])
            m[key].append(s)
        
        return list(m.values())