# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        res = float('-inf')
        ret = 0
        lev = 1
        while q:
            qLen = len(q)
            s = 0
            for i in range(qLen):
                cur = q.pop(0)
                s += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if s > res:
                res = s
                ret = lev
            lev += 1
        return ret