class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {} # (i, total)
        total = sum(stones)
        target = math.ceil(total / 2)

        def dfs(i, curSum):
            if i == len(stones) or curSum >= target:
                return abs(curSum - (total - curSum))
            
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            
            stoneNotPicked = dfs(i + 1, curSum)
            stonePicked = dfs(i + 1, curSum + stones[i])
            dp[(i, curSum)] = min(stoneNotPicked, stonePicked)
            return dp[(i, curSum)]
        
        return dfs(0, 0)

            