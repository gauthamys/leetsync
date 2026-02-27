class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        def backtrack(idx):
            if sides[0] == sides[1] == sides[2] == sides[3] == side:
                return True

            if idx >= len(matchsticks):
                return False

            for i in range(4):
                if sides[i] + matchsticks[idx] <= side:
                    sides[i] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
            
            if sides[i] == 0:
                return False
        
        return backtrack(0)
        
        
        