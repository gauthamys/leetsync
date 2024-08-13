class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        set<pair<int, int>> v;
        int res = 0;
        int ROWS = grid.size();
        int COLS = grid[0].size();
        for(int i=0; i<ROWS; i++) {
            for(int j=0; j<COLS; j++) {
                if(grid[i][j] == 1 && v.find({i, j}) == v.end()) {
                    // start dfs
                    queue<pair<int, int>> q;
                    int curArea = 0;
                    q.push({i, j});
                    v.insert({i, j});
                    while(!q.empty()) {
                        pair<int, int> cur = q.front();
                        q.pop();
                        int rowIndex = cur.first;
                        int colIndex = cur.second; 
                        curArea++;
                        if(rowIndex+1 < ROWS && grid[rowIndex + 1][colIndex] == 1 && v.find({rowIndex + 1, colIndex}) == v.end()) {
                            v.insert({rowIndex + 1, colIndex});
                            q.push({rowIndex + 1, colIndex});
                        }
                        if(rowIndex-1 >= 0 && grid[rowIndex - 1][colIndex] == 1 && v.find({rowIndex - 1, colIndex}) == v.end()) {
                            v.insert({rowIndex - 1, colIndex});
                            q.push({rowIndex - 1, colIndex});
                        }
                        if(colIndex+1 < COLS && grid[rowIndex][colIndex + 1] == 1 && v.find({rowIndex, colIndex + 1}) == v.end()) {
                            v.insert({rowIndex, colIndex + 1});
                            q.push({rowIndex, colIndex + 1});
                        }
                        if(colIndex-1 >= 0 && grid[rowIndex][colIndex - 1] == 1 && v.find({rowIndex, colIndex - 1}) == v.end()) {
                            v.insert({rowIndex, colIndex - 1});
                            q.push({rowIndex, colIndex - 1});
                        }
                    }
                    res = max(res, curArea);
                }
            }
        }
        return res;
    }
};
