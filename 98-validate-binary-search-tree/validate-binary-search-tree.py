# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = [(root, float('inf'), float('-inf'))]
        while q:
            cur, leftMax, rightMin = q.pop(0)
            if cur.val >= leftMax or cur.val <= rightMin:
                return False
            if cur.left:
                q.append([cur.left, min(leftMax, cur.val), rightMin])
            if cur.right:
                q.append([cur.right, leftMax, max(rightMin, cur.val)])
        return True
