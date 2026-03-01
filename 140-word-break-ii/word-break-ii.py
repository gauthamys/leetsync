class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtrack(start, curWord, curSentence):
            word = ''.join(curWord)
            if start >= len(s):
                if word in wordDict:
                    curSentence.append(word)
                    res.append(" ".join(curSentence))
                    curSentence.pop()
                return

            if word in wordDict:
                curSentence.append(word)
                backtrack(start + 1, [s[start]], curSentence)
                curSentence.pop()

            curWord.append(s[start])
            backtrack(start + 1, curWord, curSentence)
            curWord.pop()
        
        backtrack(0, [], [])
        return res