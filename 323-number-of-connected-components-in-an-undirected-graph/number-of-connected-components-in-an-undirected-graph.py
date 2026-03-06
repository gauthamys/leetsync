class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = node
            while p != parent[p]:
                p = parent[p]
            return p
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        
        return res
        

            

        
       