import math
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        workers.sort()
        jobs.sort()
        days = []
        for i in range(len(jobs)):
            days.append(math.ceil(jobs[i] / workers[i]))
            
        return max(days)