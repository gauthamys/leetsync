# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk = []
        if root is not None:
            stk = [(1, root)]
        
        res = 0
        while len(stk) > 0:
            curdepth, cur = stk.pop()
            if cur.left is None and cur.right is None:
                res = max(res, curdepth)

            if cur.left:
                stk.append((curdepth + 1, cur.left))
            if cur.right:
                stk.append((curdepth + 1, cur.right))
        
        return res
        

            

            
            