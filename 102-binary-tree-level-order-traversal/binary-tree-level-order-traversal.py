# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        res = []

        while q:
            l = len(q)
            tmp = []
            for i in range(len(q)):
                cur = q.pop(0)
                tmp.append(cur.val)
            
                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
            res.append(tmp)

        return res
