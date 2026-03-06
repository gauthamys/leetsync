class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        maxHeap = [-counts[t] for t in counts]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap:
            cycle = n + 1
            store = []
            task_count = 0
            while cycle > 0 and maxHeap:
                current_freq = -heapq.heappop(maxHeap)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                cycle -= 1
                task_count += 1
            for x in store:
                heapq.heappush(maxHeap, x)
            time += task_count if not maxHeap else n + 1
        
        return time


        # A, A, A, B, B, B
        # A: 3
        # B: 3
        # [(-3, A), (-3, B)]
        # A, B, idle, A, B, idle

        
        