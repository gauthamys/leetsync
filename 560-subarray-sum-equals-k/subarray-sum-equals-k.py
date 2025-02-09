class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        s = 0
        res = 0
        for n in nums:
            s += n
            if s - k in m:
                res += m[s - k]
            m[s] += 1
            
        return res
