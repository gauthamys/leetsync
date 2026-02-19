class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        return [x[0] for x in sorted(counts.items(), key=lambda y: y[1],reverse=True)][:k]
        