class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        pq = [(-count, char) for char, count in counts.items()]
        ans = []

        heapq.heapify(pq)
        while pq:
            count_first, char_first = heapq.heappop(pq)
            if len(ans) == 0 or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0:
                    heapq.heappush(pq, (count_first + 1, char_first))
            else:
                if not pq:
                    return ''
                count_second, char_second = heapq.heappop(pq)
                ans.append(char_second)
                if count_second + 1 != 0:
                    heapq.heappush(pq, (count_second + 1, char_second))
                heapq.heappush(pq, (count_first, char_first))
        
        return ''.join(ans)
