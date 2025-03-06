class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0, r=height.size()-1;
        int res = 0;
        while(l < r) {
            cout << l << " " << r << " " << res <<  endl;
            int cur = min(height[l], height[r]) * (r - l);
            if(height[l] < height[r]) {
                l++;
            }
            else{
                r--;
            }
            res = max(res, cur);
        }
        return res;
    }
};