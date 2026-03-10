class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        sums = set([0])
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                return True

            for s in sums.copy():
                if s + nums[i] == target:
                    return True
                sums.add(s + nums[i])
        
        return False