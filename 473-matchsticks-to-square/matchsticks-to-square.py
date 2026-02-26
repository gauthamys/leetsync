class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        side = total // 4
        sides = [0, 0, 0, 0]
        def backtrack(start):
            if start == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side
            
            x = matchsticks[start]
            for i in range(4):
                if sides[i] + x <= side:
                    sides[i] += x
                    if backtrack(start + 1):
                        return True
                    sides[i] -= x

                if sides[i] == 0:
                    break
            
            return False
        
        return backtrack(0)
                
            