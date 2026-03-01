class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def pattern(word):
            res = []
            for i in range(len(word)):
                res.append(word[:i] + '*' + word[i + 1:])
            return res
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pat in pattern(word):
                adj[pat].append(word)
        
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1
        
        while q:
            qLen = len(q)
            for _ in range(qLen):
                curWord = q.popleft()
                if curWord == endWord:
                    return res

                for pat in pattern(curWord):
                    for nei in adj[pat]:
                        if nei in visited or curWord not in wordList:
                            continue
                        q.append(nei)
                        visited.add(nei)
            res += 1

        return 0