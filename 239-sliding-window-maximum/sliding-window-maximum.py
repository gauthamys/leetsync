class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        
        res.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res
    
    # 1 3 -1 -3 5 3 6 7
    # dq = [3, -1]