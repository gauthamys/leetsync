class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        return ' '.join(list(reversed(s.split())))