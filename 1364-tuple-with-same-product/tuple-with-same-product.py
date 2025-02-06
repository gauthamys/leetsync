from collections import defaultdict
import math

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                products[nums[i] * nums[j]].append((nums[i], nums[j]))

        res = 0

        for p in products.keys():
            if len(products[p]) > 1:
                res += math.factorial(len(products[p])) / (2 * math.factorial(len(products[p]) - 2))
        #print(products)
        return int(res * 8)

