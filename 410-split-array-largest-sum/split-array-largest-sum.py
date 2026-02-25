class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def minimum_splits_required(max_sum_allowed):
            cur_sum = 0
            splits_required = 0
            for n in nums:
                cur_sum += n
                if cur_sum > max_sum_allowed:
                    cur_sum = n
                    splits_required += 1
            return splits_required
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if minimum_splits_required(mid) >= k:
                l = mid + 1
            else:
                r = mid
        return l