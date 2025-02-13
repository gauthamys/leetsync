# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stk = [root]
        parent = {}
        parent[root] = None
        while stk and p not in parent or q not in parent:
            cur = stk.pop()
            if cur.right:
                parent[cur.right] = cur
                stk.append(cur.right)
            if cur.left:
                parent[cur.left] = cur
                stk.append(cur.left)
        
        ancs = set()
        while p:
            ancs.add(p)
            p = parent[p]
        while q not in ancs:
            q = parent[q]
        
        return q
            



        

                
