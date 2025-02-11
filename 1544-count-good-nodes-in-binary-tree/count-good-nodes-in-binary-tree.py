# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        
        def helper(maxNum, node):
            nonlocal res
            if not node:
                return

            if node.val >= maxNum:
                res += 1
                maxNum = node.val
            helper(maxNum, node.right)
            helper(maxNum, node.left)
        
        helper(float('-inf'), root)
        return res
