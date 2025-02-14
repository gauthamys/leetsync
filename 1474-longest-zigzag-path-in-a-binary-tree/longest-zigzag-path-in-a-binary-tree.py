# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, dir, steps):
            nonlocal res

            if not node:
                return 0
            
            res = max(steps, res)
            if dir == "right":
                dfs(node.left, "left", steps + 1)
                dfs(node.right, "right", 1)
            if dir == "left":
                dfs(node.left, "left", 1)
                dfs(node.right, "right", steps + 1)
        
        dfs(root, "left", 0)
        return res
