class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 0
        return [x[0] for x in sorted(m.items(), key=lambda y: -y[1])][:k]