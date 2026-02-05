# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancs = {root: None}
        qu = [root]
        visited = set()
        visited.add(root)
        while p not in visited or q not in visited:
            cur = qu.pop(0)
            if cur.left:
                qu.append(cur.left)
                visited.add(cur.left)
                ancs[cur.left] = cur
            if cur.right:
                qu.append(cur.right)
                visited.add(cur.right)
                ancs[cur.right] = cur
        p_path = [p]
        cur = p
        while cur:
            cur = ancs[cur]
            p_path.append(cur)
        
        cur = q
        while cur not in p_path:
            cur = ancs[cur]
        return cur
            