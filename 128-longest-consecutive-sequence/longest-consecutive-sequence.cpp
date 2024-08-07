class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int res = 0;
        for(auto &n: s){
            if(!s.count(n - 1)){
                int cur = 1;
                while(s.count(n + cur)){
                    ++cur;
                }
                res = max(res, cur);
            }
        }
        return res;
    }
};