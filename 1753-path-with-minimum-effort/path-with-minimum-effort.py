class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)] # max effort, row, col
        visited = set()
        while min_heap:
            cur_max, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            
            if (r, c) == (rows - 1, cols - 1):
                return cur_max
            
            visited.add((r, c))
            for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if new_r >= rows or new_r < 0 or new_c >= cols or new_c < 0:
                    continue
                new_effort = abs(heights[r][c] - heights[new_r][new_c])
                new_effort = max(new_effort, cur_max)
                heapq.heappush(min_heap, (new_effort, new_r, new_c))

