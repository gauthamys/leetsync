class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        a_max = b_max = c_max = float('-inf')
        res = len(triplets)
        for x, y, z in triplets:
            if x > a or y > b or z > c:
                res -= 1
                continue
            a_max = max(a_max, x)
            b_max = max(b_max, y)
            c_max = max(c_max, z)

        if res == 0:
            return False

        return [a_max, b_max, c_max] == target
            