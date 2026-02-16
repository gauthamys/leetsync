class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        starts = {}
        ends = {}

        for i, c in enumerate(s):
            if c not in starts:
                starts[c] = i
            ends[c] = i

        intervals = [(starts[c], ends[c]) for c in starts]
        intervals.sort()
        
        res = []
        merged = []
        prev_start, prev_end = intervals[0]
        
        for start, end in intervals[1:]:
            if start > prev_end:
                res.append(prev_end)
                merged.append([prev_start, prev_end])
                prev_start = start    
            prev_end = max(prev_end, end)

        merged.append([prev_start, prev_end])
        return [x[1] - x[0] + 1 for x in merged]

