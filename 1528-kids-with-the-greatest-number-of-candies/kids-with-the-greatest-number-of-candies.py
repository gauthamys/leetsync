class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            res.append(candies[i] + extraCandies >= max(candies))
        return res