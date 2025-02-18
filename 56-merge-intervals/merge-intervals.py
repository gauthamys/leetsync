class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curStart = intervals[0][0]
        curEnd = intervals[0][1]

        for begin, end in intervals:
            if begin > curEnd:
                res.append([curStart, curEnd])
                curStart = begin
            curEnd = max(curEnd, end)

        res.append([curStart, curEnd])
        return res