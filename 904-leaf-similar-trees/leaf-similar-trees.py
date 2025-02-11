# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def view(node):
            if not node:
                return []
            stk = [node]
            res = []
            while stk:
                cur = stk.pop()
                if cur.left is None and cur.right is None:
                    res.append(cur.val)
                if cur.right:
                    stk.append(cur.right)
                if cur.left:
                    stk.append(cur.left)
            return res

        return view(root1) == view(root2)