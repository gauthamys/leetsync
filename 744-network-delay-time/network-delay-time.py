class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        t = [float('inf')] * n
        t[k - 1] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                t[v - 1] = min(t[v - 1], t[u - 1] + w)
        
        return max(t) if max(t) != float('inf') else -1