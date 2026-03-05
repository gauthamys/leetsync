# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(prev, node, left):
            if not node:
                return
            
            dfs(node, node.right, False)
            dfs(node, node.left, True)
            
            if not node.left and not node.right and node.val == target:
                if left:
                    prev.left = None
                else:
                    prev.right = None
        
        res = TreeNode(0, left=root)
        dfs(res, root, True)
        return res.left
        