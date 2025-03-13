class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def make_key(l):
            return '-'.join([str(i) for i in l])
        
        r = defaultdict(int)
        c = defaultdict(int)
        for i in range(len(grid)):
            r[make_key(grid[i])] += 1
        
        for j in range(len(grid[0])):
            col = [grid[r][j] for r in range(len(grid))]
            c[make_key(col)] += 1
        
        res = 0
        for l in r:
            res += r[l] * c[l]

        return int(res)

