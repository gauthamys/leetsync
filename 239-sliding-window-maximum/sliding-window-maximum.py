class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([]) # idx
        res = []
        
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        
        res.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            if i - dq[0] == k:
                dq.popleft()
            
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res
            