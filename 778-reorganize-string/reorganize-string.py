class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        l = [(-counts[c], c) for c in counts]
        heapq.heapify(l)
        
        res = []
        while l:
            count_first, char_first = heapq.heappop(l)
            if not res or res[-1] != char_first:
                res.append(char_first)
                if count_first + 1 < 0:
                    heapq.heappush(l, (count_first + 1, char_first))
                
            else:
                if not l:
                    return ""
                count_second, char_second = heapq.heappop(l)
                res.append(char_second)
                if count_second + 1 < 0:
                    heapq.heappush(l, (count_second + 1, char_second))
                heapq.heappush(l, (count_first, char_first))
        
        return "".join(res)
            
            
