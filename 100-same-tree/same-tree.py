# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q or q and not p:
            return False
        stk1 = [p]
        stk2 = [q]
        while stk1 or stk2:
            cur1 = stk1.pop()
            cur2 = stk2.pop()
            if cur1.val != cur2.val:
                return False
            if cur1.left and cur2.left:
                stk1.append(cur1.left)
                stk2.append(cur2.left)
            if cur1.right and cur2.right:
                stk1.append(cur1.right)
                stk2.append(cur2.right)
            if cur1.left and not cur2.left:
                return False
            if cur1.right and not cur2.right:
                return False
            if cur2.left and not cur1.left:
                return False
            if cur2.right and not cur1.right:
                return False

        return True
