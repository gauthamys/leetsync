class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        pq = [(-counts[v], v) for v in counts]
        heapq.heapify(pq)
        time = 0

        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            while cycle > 0 and pq:
                current_freq, current_task = heapq.heappop(pq)
                current_freq = -current_freq
                if current_freq > 1:
                    store.append((-(current_freq - 1), current_task))
                task_count += 1
                cycle -= 1
            
            for x in store:
                heapq.heappush(pq, x)
            
            time += task_count if not pq else n + 1
        
        return time
            


        