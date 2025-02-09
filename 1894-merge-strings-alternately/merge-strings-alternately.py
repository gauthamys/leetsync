class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1: return word2
        if not word2: return word1
        
        p1 = p2 = 0
        res = ''
        while p1 < len(word1) and p2 < len(word2):
            res += word1[p1]
            p1 += 1
            res += word2[p2]
            p2 += 1
        
        if p1 < len(word1):
            while p1 < len(word1):
                res += word1[p1]
                p1 += 1
        
        if p2 < len(word2):
            while p2 < len(word2):
                res += word2[p2]
                p2 += 1
        
        return res