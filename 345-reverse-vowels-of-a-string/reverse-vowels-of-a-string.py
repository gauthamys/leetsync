class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        stk = []
        q = []

        for i, c in enumerate(s):
            if c in vowels:
                stk.append(c)
                
        l = list(s)
        for i, c in enumerate(l):
            if c in vowels:
                l[i] = stk.pop()

        return ''.join(l)

        

            