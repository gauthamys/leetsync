class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtrack(idx, curWord, curSentence):
            word = ''.join(curWord)
            if idx == len(s):
                if word in wordDict:
                    curSentence.append(word)
                    res.append(' '.join(curSentence))
                    curSentence.pop()
                return
            
            if word in wordDict:
                curSentence.append(word)
                cur = [s[idx]]
                backtrack(idx + 1, cur, curSentence)
                cur = list(word)
                curSentence.pop()
            
            curWord.append(s[idx])
            backtrack(idx + 1, curWord, curSentence)
            curWord.pop()
        
        backtrack(0, [], [])
        return res
