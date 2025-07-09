// DFS solution
class Solution {
public:
    double dfs(string a, string b, unordered_map<string, vector<string>>& graph, 
               map<pair<string,string>, double>& quotient, unordered_set<string>& visited) {
        if (a == b) return 1.0;
        
        visited.insert(a);
        
        for (auto nxt : graph[a]) {
            if (visited.count(nxt)) continue;
            
            double x = dfs(nxt, b, graph, quotient, visited);
            if (x > 0) {
                return x * quotient[{a, nxt}];
            }
        }
        
        return -1.0;
    }
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, vector<string>> graph;
        map<pair<string,string>, double> quotient;
        
        for (int i = 0; i < equations.size(); i++) {
            string a = equations[i][0], b = equations[i][1];
            graph[a].push_back(b);
            graph[b].push_back(a);
            
            quotient[{a, b}] = values[i];     // a/b = value
            quotient[{b, a}] = 1.0 / values[i]; // b/a = 1/value
        }
        
        vector<double> res;
        for (auto query : queries) {
            string a = query[0], b = query[1];
            
            // Check if both variables exist in the graph
            if (graph.find(a) == graph.end() || graph.find(b) == graph.end()) {
                res.push_back(-1.0);
                continue;
            }
            
            if (a == b) {
                res.push_back(1.0);
            } else {
                unordered_set<string> visited;
                double x = dfs(a, b, graph, quotient, visited);
                res.push_back(x);
            }
        }
        return res;
    }
};