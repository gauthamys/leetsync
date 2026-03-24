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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return root;
        }
        if (root.val == key) {
            if(root.right == null) {
                return root.left;
            }
            if(root.left == null) {
                return root.right;
            }
            TreeNode cur = root.right;
            while (cur.left != null) {
                cur = cur.left;
            }
            root.val = cur.val;
            root.right = this.deleteNode(root.right, root.val);
        }
        else if (root.val < key) {
            root.right = this.deleteNode(root.right, key);
        } 
        else {
            root.left = this.deleteNode(root.left, key);
        }
        return root;
    }
}