class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(point):
            return abs(point[0] - target[0]) + abs(point[1] - target[1])
        DIST = abs(target[0]) + abs(target[1])
        for point in ghosts:
            if dist(point) <= DIST:
                return False
        return True