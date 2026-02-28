"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {} # n.val: Node
        def copy(n):
            if n.val in visited:
                return visited[n.val]
            
            res = Node(n.val)
            visited[res.val] = res
            
            for nei in n.neighbors:
                res.neighbors.append(copy(nei))
            
            return res
            
        
        return copy(node)