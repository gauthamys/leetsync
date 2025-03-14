class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        endings = defaultdict(int)
        wall_len = sum(wall[0])
        for row in wall:
            cur_end = 0
            for brick in row:
                cur_end += brick
                endings[cur_end] += 1
        
        print(endings)
        max_end = 0
        for end in endings:
            if endings[end] > max_end and end < wall_len:
                max_end = endings[end]
            
        return len(wall) - max_end