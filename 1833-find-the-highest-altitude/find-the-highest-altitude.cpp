class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int prefix = 0;
        int res = 0;
        for(int alt: gain) {
            prefix = prefix + alt;
            res = max(res, prefix);
        }
        return res;
    }
};