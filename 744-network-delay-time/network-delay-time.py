class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delays = [float('inf')] * n
        delays[k - 1] = 0
        
        for _ in range(n - 1):
            for u, v, w in times:
                delays[v - 1] = min(delays[v - 1], delays[u - 1] + w)
        
        res = max(delays)
        return res if res != float('inf') else -1