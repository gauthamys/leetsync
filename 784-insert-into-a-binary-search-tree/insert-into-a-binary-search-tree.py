# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        anc = None
        while node:
            anc = node
            if val > node.val:
                node = node.right
            elif val < node.val:
                node = node.left
        if val < anc.val:
            anc.left = TreeNode(val)
        elif val > anc.val:
            anc.right = TreeNode(val)
        return root