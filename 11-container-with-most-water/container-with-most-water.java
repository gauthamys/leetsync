class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int res = 0;
        while (l < r) {
            int cur = (r - l) * Math.min(height[r], height[l]);
            if (height[l] > height[r]) {
                r -= 1;
            } else {
                l += 1;
            }
            res = Math.max(cur, res);
        }
        return res;
    }
}