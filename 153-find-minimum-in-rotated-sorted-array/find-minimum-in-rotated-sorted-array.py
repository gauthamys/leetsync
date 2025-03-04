class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print(l, r)
            mid = (l + r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid