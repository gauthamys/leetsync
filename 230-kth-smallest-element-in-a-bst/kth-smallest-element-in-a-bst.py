# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = [root]
        res = root.val
        visited = set()
        cnt = 0
        while stk:
            cur = stk[-1]
            print(cur.val, cnt, [x.val for x in stk])
            if cur.left and cur.left not in visited:
                stk.append(cur.left)
                visited.add(cur.left)
            else:
                stk.pop()
                cnt += 1
                if cnt == k:
                    return cur.val
                if cur.right:
                    stk.append(cur.right)