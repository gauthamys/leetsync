class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        maxHeap = [-counts[t] for t in counts]
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap:
            stored = []
            cycle = n + 1
            task_count = 0
            
            while maxHeap and cycle > 0:
                cur_freq = heapq.heappop(maxHeap)
                task_count += 1
                cycle -= 1
                if cur_freq < -1:
                    stored.append(cur_freq + 1)
            
            for f in stored:
                heapq.heappush(maxHeap, f)
            
            time += task_count if not maxHeap else n + 1
        
        return time
