class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            flag = (r - mid) % 2 == 0
            if nums[mid] == nums[mid + 1]:
                if flag:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if flag:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]