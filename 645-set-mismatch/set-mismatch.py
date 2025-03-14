class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        res = [-1, -1]
        for n in nums:
            if n in seen:
                res[0] = n
            else:
                seen.add(n)
        
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res[1] = i
        
        return res
            