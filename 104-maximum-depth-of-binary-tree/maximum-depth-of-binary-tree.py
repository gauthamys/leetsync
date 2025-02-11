# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stk = [(root, 1)]
        res = 1
        while stk:
            cur, d = stk.pop()
            res = max(res, d)
            if cur.right:
                stk.append((cur.right, 1 + d))
            if cur.left:
                stk.append((cur.left, 1 + d))
        
        return res
            