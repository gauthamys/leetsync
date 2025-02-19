# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = dict()
        parent[root] = None
        qu = [root]
        while qu and p not in parent or q not in parent:
            cur = qu.pop(0)
            if cur.right:
                qu.append(cur.right)
                parent[cur.right] = cur
            if cur.left:
                qu.append(cur.left)
                parent[cur.left] = cur
        
        ancs = set()
        while p:
            ancs.add(p)
            p = parent[p]
        
        while q not in ancs:
            q = parent[q]
        
        return q