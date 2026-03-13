class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            for s in subsets.copy():
                subsets.append(s + [n])
        return subsets