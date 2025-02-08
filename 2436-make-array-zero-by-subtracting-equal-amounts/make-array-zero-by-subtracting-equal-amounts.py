class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)) if 0 not in set(nums) else len(set(nums)) - 1