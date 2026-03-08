class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def patterns(word):
            res = []
            for i in range(len(word)):
                res.append(word[:i] + '*' + word[i+1:])
            return res
        
        if endWord not in wordList:
            return 0
        
        wordList.append(endWord)
        adj = defaultdict(list)
        for w in wordList:
            for p in patterns(w):
                adj[p].append(w)
        
        q = deque([(beginWord, 1)]) # word, pathlength
        visited = set()
        visited.add(beginWord)
        while q:
            cur, l = q.popleft()
            if cur == endWord:
                return l

            for p in patterns(cur):
                for nei in adj[p]:
                    if nei in visited:
                        continue
                    q.append((nei, l + 1))
                    visited.add(nei)
        
        return 0