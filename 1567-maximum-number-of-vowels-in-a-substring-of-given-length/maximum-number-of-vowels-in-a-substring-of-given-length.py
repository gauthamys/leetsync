class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur = 0
        l = 0
        r = k - 1
        for i in range(k):
            if s[i] in 'aeiou':
                cur += 1
        res = cur

        while r < len(s) - 1:
            r += 1
            if s[r] in 'aeiou':
                cur += 1
            if s[l] in 'aeiou':
                cur -= 1
            l += 1
            res = max(res, cur)
        
        return res