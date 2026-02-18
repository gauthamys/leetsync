class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid + 1]:
                # remove (mid, mid + 1)
                # if left is odd go there, if right is odd go there
                if (r - mid - 1) % 2 == 1:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if (mid - 1 - l) % 2 == 1:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]