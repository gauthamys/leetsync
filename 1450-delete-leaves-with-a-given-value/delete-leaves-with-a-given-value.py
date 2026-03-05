# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete(parent, node, left):
            if not node:
                return
            
            delete(node, node.left, True)
            delete(node, node.right, False)

            if (node.left, node.right, node.val) == (None, None, target):
                if left:
                    parent.left = None
                else:
                    parent.right = None
        
        res = TreeNode(0, left=root)
        delete(res, root, True)

        return res.left