class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        subsets = set()
        subsets.add(0)
        for i in range(len(nums) - 1, -1, -1):
            if target in subsets:
                return True
            for s in subsets.copy():
                curSum = s + nums[i]
                if curSum not in subsets:
                    subsets.add(curSum)
        
        return False 