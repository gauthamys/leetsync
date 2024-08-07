class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
       vector<set<int>> rows(9);
       vector<set<int>> cols(9);
       vector<set<int>> sub(9);

        for(int i=0; i<board.size(); i++) {
            for(int j=0; j<board[0].size(); j++) {
                int cur = board[i][j];
                if(cur == (int)'.') continue;
                
                int subIndex = 3 * (i / 3) + j / 3;

                if(rows[i].find(cur) != rows[i].end() || 
                   cols[j].find(cur) != cols[j].end() ||
                   sub[subIndex].find(cur) != sub[subIndex].end()) {

                    return false;
                }
                rows[i].insert(cur);
                cols[j].insert(cur);
                sub[subIndex].insert(cur);
            }
        }
        return true;
    }
};