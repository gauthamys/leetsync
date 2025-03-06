class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        stack<int> stk;
        set<int> visited;
        stk.push(0);
        while(!stk.empty()) {
            int cur = stk.top();
            stk.pop();
            visited.insert(cur);
            for(auto key: rooms[cur]) {
                if(visited.find(key) == visited.end()) {
                    stk.push(key);
                }
            }
        }
        return visited.size() == rooms.size();
    }
};