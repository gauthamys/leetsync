# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = [[root, float('inf'), float('-inf')]]
        while q:
            cur, left_max, right_min = q.pop(0)
            if cur.val <= right_min or cur.val >= left_max:
                return False
            if cur.left:
                q.append([cur.left, min(left_max, cur.val), right_min])
            if cur.right:
                q.append([cur.right, left_max, max(right_min, cur.val)])
        return True