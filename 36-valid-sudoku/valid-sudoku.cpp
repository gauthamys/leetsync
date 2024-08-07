class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
       vector<set<char>> rows(9);
       vector<set<char>> cols(9);
       vector<set<char>> sub(9);

        for(int i=0; i<board.size(); i++) {
            for(int j=0; j<board[0].size(); j++) {
                char cur = board[i][j];
                if(cur == '.') continue;
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