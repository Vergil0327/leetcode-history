using pdi = pair<double,int>;

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        int n = classes.size();
        priority_queue<pdi> pq; // max heap
        for (int i=0; i<n; i++) {
            double pass = classes[i][0], total = classes[i][1];
            double next_gain = ((pass+1) / (total+1)) - pass/total;
            pq.push({next_gain, i});
        }

        for (int i=0; i<extraStudents; i++) {
            int idx = pq.top().second;
            pq.pop();
            
            classes[idx][0]++;
            classes[idx][1]++;
            double pass = classes[idx][0], total = classes[idx][1];
            double next_gain = ((pass+1) / (total+1)) - pass/total;
            
            pq.push({next_gain, idx});
        }

        double res = 0;
        while (!pq.empty()) {
            int i = pq.top().second;
            pq.pop();
            res += (double) classes[i][0]/classes[i][1];
        }
        return res / n;
    }
};
