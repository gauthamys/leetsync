# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete(par, node, left):
            if not node:
                return
            delete(node, node.left, True)
            delete(node, node.right, False)
            if node.val == target and not node.left and not node.right:
                if left:
                    par.left = None
                else:
                    par.right = None
        
        res = TreeNode(0, left=root)
        delete(res, res.left, True)
        return res.left
            