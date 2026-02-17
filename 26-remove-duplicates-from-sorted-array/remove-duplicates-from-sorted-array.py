class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insert = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[insert] = nums[i]
                insert += 1
        return insert
