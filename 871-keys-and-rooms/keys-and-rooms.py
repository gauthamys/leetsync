class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i, keys in enumerate(rooms):
            adj[i].extend(keys)
            
        stk = [0]
        visited = set()
        while(stk):
            cur = stk.pop()
            visited.add(cur)
            for nei in adj[cur]:
                if nei not in visited:
                    stk.append(nei)
        
        return len(visited) == len(rooms)
        
