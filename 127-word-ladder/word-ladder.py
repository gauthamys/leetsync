from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def pattern(word):
            patterns = []
            for j in range(len(word)):
                patterns.append(word[:j] + "*" + word[j + 1:])
            return patterns

        adj = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for pat in pattern(w):
                adj[pat].append(w)

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1

        while q:
            qLen = len(q)
            for _ in range(qLen):
                cur = q.popleft()
                if cur == endWord:
                    return res
                
                for pat in pattern(cur):
                    for nei in adj[pat]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        visited.add(nei)
            res += 1
        
        return 0