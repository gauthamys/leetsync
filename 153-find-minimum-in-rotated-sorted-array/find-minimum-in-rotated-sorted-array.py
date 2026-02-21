class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[l]
        return nums[l]
        