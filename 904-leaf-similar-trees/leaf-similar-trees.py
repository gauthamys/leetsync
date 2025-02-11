# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get(node):
            if not node:
                return []

            seq = []
            if node.left:
                seq += get(node.left)
            if node.left is None and node.right is None:
                seq.append(node.val)
            if node.right:
                seq += get(node.right)
            return seq
        return get(root1) == get(root2)