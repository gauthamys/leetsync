# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        par = {root: None}
        qu = deque([root])
        visited = set([root])
        while q not in visited or p not in visited:
            cur = qu.popleft()
            if cur.left:
                qu.append(cur.left)
                visited.add(cur.left)
                par[cur.left] = cur
            if cur.right:
                qu.append(cur.right)
                visited.add(cur.right)
                par[cur.right] = cur
        
        p_path = []
        cur = p
        while cur:
            p_path.append(cur)
            cur = par[cur]
        
        cur = q
        while cur not in p_path:
            cur = par[cur]
        
        return cur
