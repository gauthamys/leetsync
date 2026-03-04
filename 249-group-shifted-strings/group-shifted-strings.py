class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = {}
        
        for s in strings:
            key = ''
            for i in range(len(s)):
                key += str((ord(s[i]) - ord(s[0])) % 26 + ord('a'))
            m[key] = m.get(key, [])
            m[key].append(s)
        
        return list(m.values())