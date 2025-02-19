class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        curStart, curEnd = intervals[0]
        res = []
        for begin, end in intervals:
            if begin > curEnd:
                res.append([curStart, curEnd])
                curStart = begin
            curEnd = max(curEnd, end)
        res.append([curStart, curEnd])
        return res