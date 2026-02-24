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
            dfs(node, node.left, True)
            dfs(node, node.right, False)
            if not node.left and not node.right and node.val == target:
                if left:
                    prev.left = None
                else:
                    prev.right = None
                return
        root_parent = TreeNode(0, left=root)
        dfs(root, root_parent, True)
        return root_parent.left