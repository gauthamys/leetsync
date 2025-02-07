class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            res.append(candies[i] == max(candies))
            candies[i] -= extraCandies
        
        return res
