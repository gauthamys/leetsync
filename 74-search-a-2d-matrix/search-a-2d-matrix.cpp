class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        int t=0, b=rows-1;
        while(t <= b) {
            int midR = (t + b) / 2;
            if(target > matrix[midR][cols - 1]) {
                t = midR + 1;
            } else if(target < matrix[midR][0]){
                b = midR - 1;
            } else {
                break;
            }
        }
        if(t > b) return false;

        int l=0, r=cols-1;
        int midR = (t + b) / 2;
        while(l <= r) {
            int midC = (l + r) / 2;
            if(target > matrix[midR][midC]) {
                l = midC + 1;
            }
            else if(target < matrix[midR][midC]) {
                r = midC - 1;
            }
            else {
                return true;
            }
        }
        return false;
    }   
};
