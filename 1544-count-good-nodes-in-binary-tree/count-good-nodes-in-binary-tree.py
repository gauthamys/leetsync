# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = [[root, root.val]]
        res = 0
        while stk:
            cur_node, cur_max = stk.pop()
            if cur_node.val >= cur_max:
                res += 1
            if cur_node.left:
                stk.append([cur_node.left, max(cur_node.val, cur_max)])
            if cur_node.right:
                stk.append([cur_node.right, max(cur_node.val, cur_max)])
        return res