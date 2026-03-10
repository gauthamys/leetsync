class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def pattern(word):
            return [''.join(word[:i]) + '*' + ''.join(word[i + 1:]) for i in range(len(word))]
        
        if endWord not in wordList:
            return 0
        
        adj = {}
        wordList.append(beginWord)
        for word in wordList:
            for p in pattern(word):
                if p not in adj:
                    adj[p] = []
                adj[p].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            cur, steps = q.popleft()

            if cur == endWord:
                return steps

            for p in pattern(cur):
                for nei in adj[p]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append((nei, steps + 1))
                
        return 0