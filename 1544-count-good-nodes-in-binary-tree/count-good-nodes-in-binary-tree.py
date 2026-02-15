# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = [(root, root.val)]
        res = 0
        while stk:
            cur, curMax = stk.pop()
            if cur.val >= curMax:
                res += 1
                curMax = cur.val
            if cur.left:
                stk.append((cur.left, curMax))
            if cur.right:
                stk.append((cur.right, curMax))
        return res