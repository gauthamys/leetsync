class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        q, farthest = deque([0]), 0
        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(len(s), i + maxJump + 1)):
                if s[j] == '0':
                    if j == len(s) - 1:
                        return True
                    q.append(j)
            farthest = i + maxJump 
                

        return False