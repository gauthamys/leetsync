class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res = "";
        int w1 = 0, w2 = 0;
        while(w1 < word1.length() || w2 < word2.length()) {
            if(w1 == word1.length()) {
                while(w2 < word2.length()) {
                    res = res + word2[w2];
                    w2++;
                }
            }
            else if(w2 == word2.length()) {
                while(w1 < word1.length()) {
                    res = res + word1[w1];
                    w1++;
                }
            }
            else {
                res = res + word1[w1] + word2[w2];
                w1++;
                w2++;
            }
            
        }
        
        return res;
    }
};