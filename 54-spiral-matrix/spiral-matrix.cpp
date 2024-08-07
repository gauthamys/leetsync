class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int ROWS = matrix.size();
        int COLS = matrix[0].size();
        int t = 0, b = ROWS - 1;
        int l = 0, r = COLS - 1;
        string direction = "right";
        while(l <= r && t <= b) {
            if(direction == "right") {
                for(int i=l; i<=r; i++) {
                    res.push_back(matrix[t][i]);
                }
                t++;
                direction = "down";
            }
            else if(direction == "down") {
                for(int i=t; i<=b; i++) {
                    res.push_back(matrix[i][r]);
                }
                r--;
                direction = "left";
            }
            else if(direction == "left") {
                for(int i=r; i >= l; i--) {
                    res.push_back(matrix[b][i]);
                }
                b--;
                direction = "top";
            }
            else if(direction == "top") {
                for(int i=b; i >= t; i--) {
                    res.push_back(matrix[i][l]);
                }
                l++;
                direction = "right";
            }
        }  
        return res;
    }
};