# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = [(root, float('-inf'))]
        res = 0
        while q:
            cur, curMax = q.pop(0)
            if cur.val >= curMax:
                res += 1
            curMax = max(cur.val, curMax)
            if cur.left:
                q.append([cur.left, curMax])
            if cur.right:
                q.append([cur.right, curMax])
        return res