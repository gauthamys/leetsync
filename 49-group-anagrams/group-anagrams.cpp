class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> m;
        vector<vector<string>> res;
        for(string str: strs) {
            m[generateKey(str)].push_back(str);
        }
        for(auto it=m.begin(); it != m.end(); it++) {
            res.push_back(it->second);
        }
        return res;
    }
private:
    vector<int> generateKey(string str) {
        vector<int> key(26);
        for(char s:str) {
            key[s - 'a']++;
        }
        return key;
    }
};