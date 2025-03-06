/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int longestZigZag(TreeNode* root) {
        stack<tuple<TreeNode*, int, bool>> stk;
        stk.push(make_tuple(root, 0, false));
        int res = 0;
        while(stk.size() > 0) {
            auto cur = stk.top();
            stk.pop();
            TreeNode* node = get<0>(cur);
            int steps = get<1>(cur);
            bool fromLeft = get<2>(cur);
            res = max(res, steps);
            if(node->left) {
                if(fromLeft) stk.push(make_tuple(node->left, 1, true));
                else stk.push(make_tuple(node->left, steps + 1, true));
            }
            if(node->right) {
                if (fromLeft) stk.push(make_tuple(node->right, steps + 1, false));
                else stk.push(make_tuple(node->right, 1, false));
            }
        }
        return res;
    }
};