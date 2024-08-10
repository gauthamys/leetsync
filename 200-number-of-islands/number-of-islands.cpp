class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        int res = 0;
        set<pair<int, int>> visited;
        for(int i=0; i<ROWS; i++) {
            for(int j=0; j<COLS; j++) {
                if(grid[i][j] == '1' && visited.find({i, j}) == visited.end()) {
                    // start dfs
                    stack<pair<int, int>> stk;
                    stk.push({i, j});
                    visited.insert({i, j});
                    while(!stk.empty()) {
                        pair<int, int> top = stk.top();
                        stk.pop();
                        if(top.second + 1 < COLS && grid[top.first][top.second + 1] == '1' && visited.find({top.first, top.second + 1}) == visited.end()) {
                            stk.push({top.first, top.second + 1});
                            visited.insert({top.first, top.second + 1});
                        }
                        if(top.first + 1 < ROWS && grid[top.first + 1][top.second] == '1' && visited.find({top.first + 1, top.second}) == visited.end()) {
                            stk.push({top.first + 1, top.second});
                            visited.insert({top.first + 1, top.second});
                        }
                        if(top.second - 1 >= 0 && grid[top.first][top.second - 1] == '1' && visited.find({top.first, top.second - 1}) == visited.end()) {
                            stk.push({top.first, top.second - 1});
                            visited.insert({top.first, top.second - 1});
                        }
                        if(top.first - 1 >= 0 && grid[top.first - 1][top.second] == '1' && visited.find({top.first - 1, top.second}) == visited.end()) {
                            stk.push({top.first - 1, top.second});
                            visited.insert({top.first - 1, top.second});
                        }
                    }
                    res++;

                }
            }
        }
        return res;
    }
};
