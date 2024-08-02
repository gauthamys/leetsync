class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> m;
        vector<int> res;
        for(auto num:nums) {
            m[num] = 1 + m[num];
        }
        vector<vector<int>> freq(nums.size());
        for(auto it=m.begin(); it != m.end(); ++it) {
            freq[it->second - 1].push_back(it->first);
        }
        for(int i=freq.size() - 1; i>=0; i--) {
            for(int n:freq[i]) {
                res.push_back(n);
                if(res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
