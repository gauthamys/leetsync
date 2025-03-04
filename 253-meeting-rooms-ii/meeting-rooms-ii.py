class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begins = list(sorted(i[0] for i in intervals))
        endings = list(sorted(i[1] for i in intervals))

        b, e = 0, 0
        curCount = 0
        res = 0

        while b < len(begins) and e < len(endings):
            if begins[b] < endings[e]:
                curCount += 1
                b += 1
            else:
                curCount -= 1
                e += 1
            res = max(res, curCount)

        return res