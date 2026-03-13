class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def possible(T):
            n = len(grid)
            stk = [(0, 0)]
            visited = {(0, 0)}

            while stk:
                r, c = stk.pop()
                if (r, c) == (n - 1, n - 1):
                    return True

                for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= new_r < n and 0 <= new_c < n and (new_r, new_c) not in visited and grid[new_r][new_c] <= T:
                        stk.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
            return False
        
        n = len(grid)
        l, r = grid[0][0], n * n
        while l < r:
            mid = (l + r) // 2
            if not possible(mid):
                l = mid + 1
            else:
                r = mid
        
        return l
