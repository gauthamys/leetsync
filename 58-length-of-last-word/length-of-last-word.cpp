class Solution {
public:
    int lengthOfLastWord(string s) {
        int r = s.size() - 1;
        int l = r;
        while (s[r] == ' ') {
            r--;
            l--;
        }
        while(l > -1) {
            if(s[l] == ' ') {
                return r - l;
            }
            l--;
        }
        return r - l;
    }
};