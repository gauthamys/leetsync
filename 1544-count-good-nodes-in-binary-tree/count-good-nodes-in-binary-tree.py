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
            cur, cur_max = stk.pop()
            if cur.left:
                stk.append((cur.left, max(cur_max, cur.val)))
            if cur.right:
                stk.append((cur.right, max(cur_max, cur.val)))
            if cur.val >= cur_max:
                res += 1
        return res