# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, target):
            if not node:
                return None
            if target > node.val:
                node.right = delete(node.right, target)
            elif target < node.val:
                node.left = delete(node.left, target)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                else:
                    cur = node.left
                    while cur.right:
                        cur = cur.right
                    node.val = cur.val
                    node.left = delete(node.left, node.val)
            return node
        
        return delete(root, key)
            