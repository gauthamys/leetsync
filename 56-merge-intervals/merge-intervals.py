class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        curStart = intervals[0][0]
        curEnd = intervals[0][1]
        print(intervals)
        for interval in intervals:
            print(curStart, curEnd)
            if interval[0] > curEnd:
                res.append([curStart, curEnd])
                #res.append(interval)
                curStart = interval[0]
                curEnd = interval[1]
            else:
                curStart = min(curStart, interval[0])
                curEnd = max(curEnd, interval[1])

        res.append([curStart, curEnd])
        return res
                