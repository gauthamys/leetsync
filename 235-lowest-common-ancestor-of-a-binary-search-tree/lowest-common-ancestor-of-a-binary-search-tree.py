# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        qu = [root]
        found = 0
        while qu and found != 2:
            cur = qu.pop(0)
            if cur == p:
                found += 1
            if cur == q:
                found += 1
            if cur.left:
                parent[cur.left] = cur
                qu.append(cur.left)
            if cur.right:
                parent[cur.right] = cur
                qu.append(cur.right)
        
        p_par = parent[p]
        q_par = parent[q]
        p_path = [p]
        q_path = [q]
        while p_par:
            p_path.append(p_par)
            p_par = parent[p_par]
        while q_par:
            q_path.append(q_par)
            q_par = parent[q_par]
        
        for i in range(len(p_path)):
            if p_path[i] in q_path:
                return p_path[i]
        
        
            
        