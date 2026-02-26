class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False
        
        subsets = [0] * k
        size = total // k
        nums.sort(reverse=True)

        def backtrack(start):
            if start == len(nums):
                return all(x == size for x in subsets)
            
            candidate = nums[start]
            for i in range(k):
                if subsets[i] + candidate <= size:
                    subsets[i] += candidate
                    if backtrack(start + 1):
                        return True
                    subsets[i] -= candidate
                
                if subsets[i] == 0:
                    break
            
            return False
        
        return backtrack(0)