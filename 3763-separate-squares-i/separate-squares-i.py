class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculate_areas(y_split):
            above, below = 0, 0
            for x, y, l in squares:
                if y >= y_split:
                    above += l ** 2
                else:
                    if (y + l) <= y_split:
                        below += l ** 2
                    else:
                        below += (y_split - y) * l
                        above += ((y + l) - y_split) * l
            return above, below
        
        l, r = min(y for _, y, _  in squares), max(y + side for _, y, side in squares)

        eps = 1e-6
        while r - l > eps:
            mid = (r + l) / 2.0
            area_above, area_below = calculate_areas(mid)
            if area_below < area_above:
                l = mid
            else:
                r = mid
        
        return (l + r) / 2.0