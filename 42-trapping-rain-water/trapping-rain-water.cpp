class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int res = 0;
        int leftMax = height[l];
        int rightMax = height[r];
        
        while(l < r) {
            if(leftMax < rightMax) {
                l++;
                leftMax = max(height[l], leftMax);
                res = res + (leftMax - height[l]);
            } else {
                r--;
                rightMax = max(height[r], rightMax);
                res = res + (rightMax - height[r]);
            }
        }
        return res;

    }
};
