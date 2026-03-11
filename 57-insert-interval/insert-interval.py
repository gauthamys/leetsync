class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.sort(key=lambda x: x[0])
        
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] > newInterval[0]:
                r = mid - 1
            else:
                l = mid + 1
        if newInterval[0] > intervals[mid][0]:
            mid += 1
        intervals.insert(mid, newInterval)

        curStart, curEnd = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals[1:]:
            if start > curEnd:
                res.append([curStart, curEnd])
                curStart = start
            
            curEnd = max(end, curEnd)
        
        res.append([curStart, curEnd])
        return res
            
        