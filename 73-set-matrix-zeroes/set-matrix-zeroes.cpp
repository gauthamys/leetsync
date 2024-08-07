class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        set<pair<int, int>> s;
        for(int i=0; i<matrix.size(); i++) {
            for(int j=0; j<matrix[0].size(); j++) {
                if(matrix[i][j] == 0){
                    s.insert(make_pair(i, j));
                }
            }
        }
        for(auto p:s) {
            for(int i=0; i<matrix.size(); i++) {
                matrix[i][p.second] = 0;
            }
            for(int j=0; j<matrix[0].size(); j++) {
                matrix[p.first][j] = 0;
            }
        }
    }
};