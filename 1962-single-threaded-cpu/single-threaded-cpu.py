class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pq = []
        curTime = 1
        res = []
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key=lambda x: x[0])
        pq = []
        res = []
        i = 0
        time = tasks[0][0]

        while pq or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not pq:
                time = tasks[i][0]
            else:
                procTime, idx = heapq.heappop(pq)
                time += procTime
                res.append(idx)
        
        return res
            
            