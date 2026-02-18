class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                h = i + 1
                n = 1
                while h < len(haystack) and n < len(needle) and haystack[h] == needle[n]:
                    h += 1
                    n += 1
                if n == len(needle):
                    return i
        return -1