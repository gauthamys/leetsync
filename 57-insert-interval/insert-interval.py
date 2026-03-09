class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)
        curStart, curEnd = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals[1:]:
            if start > curEnd:
                res.append([curStart, curEnd])
                curStart = start
            
            curEnd = max(end, curEnd)
        
        res.append([curStart, curEnd])
        return res
            
        