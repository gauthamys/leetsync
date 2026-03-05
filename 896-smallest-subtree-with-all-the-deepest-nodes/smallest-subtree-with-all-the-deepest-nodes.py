# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        memo = {None: 0} # node : depth
        def dfs(node):
            if node in memo:
                return memo[node]
            
            left = dfs(node.left)
            right = dfs(node.right)
            memo[node] = 1 + max(left, right)
            return memo[node]
        
        maxDepth = dfs(root)

        q = deque([(root, 1)])
        while q:
            qLen = len(q)
            for _ in range(qLen):
                cur, depth = q.popleft()
                if memo[cur.left] == memo[cur.right]:
                    if depth + memo[cur] - 1 == maxDepth:
                        return cur
                    else:
                        continue

                if memo[cur.right] > memo[cur.left]:
                    q.append((cur.right, depth + 1))
                else:
                    q.append((cur.left, depth + 1))
        


            