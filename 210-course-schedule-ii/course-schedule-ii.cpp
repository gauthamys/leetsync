class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj;
        vector<int> indegree(numCourses, 0);
        queue<int> q;
        vector<int> res;
        for(auto pre: prerequisites) {
            int src = pre[0];
            int dest = pre[1];
            adj[src].push_back(dest);
            indegree[dest]++;
        }
        for(int i=0; i<numCourses; i++) {
            if(indegree[i]==0) q.push(i);
        }
        int finished = 0;
        while(!q.empty()) {
            int cur = q.front();
            q.pop();
            for(int nei: adj[cur]) {
                indegree[nei]--;
                if(indegree[nei] == 0) {
                    q.push(nei);
                }
            }
            finished++;
            res.push_back(cur);
        }
        reverse(res.begin(), res.end());
        if(finished == numCourses) {
            return res;
        } else {
            return {};
        }
    }
};