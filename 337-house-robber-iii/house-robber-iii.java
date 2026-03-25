/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> dfs(TreeNode node) {
        if (node == null) {
            return List.of(0, 0);
        }
        List<Integer> left = this.dfs(node.left);
        List<Integer> right = this.dfs(node.right);
        int rob = node.val + left.get(1) + right.get(1);
        int notRob = Collections.max(left) + Collections.max(right);
        return List.of(rob, notRob);
    }
    public int rob(TreeNode root) {
        return Collections.max(this.dfs(root));
    }
}