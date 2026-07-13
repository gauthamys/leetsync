class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = list(range(1, 10))
        for x in q:
            d = x % 10
            if d < 9:
                q.append((x * 10) + (d + 1))
        return [x for x in q if low <= x <= high]