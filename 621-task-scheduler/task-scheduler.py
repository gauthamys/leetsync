class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-counts[t] for t in counts]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap:
            cycle = n + 1
            task_count = 0
            store = []
            while maxHeap and cycle > 0:
                current_freq = heapq.heappop(maxHeap)
                if current_freq < -1:
                    store.append(current_freq + 1)
                cycle -= 1
                task_count += 1

            for new_freq in store:
                heapq.heappush(maxHeap, new_freq)
            
            time += task_count if not maxHeap else n + 1
        
        return time
