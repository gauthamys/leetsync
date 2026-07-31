class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int leftMax = height[l];
        int rightMax = height[r];
        int res = 0;
        while (l < r) {
            leftMax = Math.max(height[l], leftMax);
            rightMax = Math.max(height[r], rightMax);
            res +=  (leftMax - height[l]) + (rightMax - height[r]);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return res;
    }
}