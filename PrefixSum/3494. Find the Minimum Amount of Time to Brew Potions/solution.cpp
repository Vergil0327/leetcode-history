class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        if (skill.empty() || mana.empty()) return 0;

        int n = skill.size(), m = mana.size();
        
        // Compute prefix sum of skills
        vector<long long> prefix_sum(n);
        partial_sum(skill.begin(), skill.end(), prefix_sum.begin());

        // Track completion times for each worker
        vector<long long> finish_times(n, 0);// Process each task
        for (int j = 0; j < m; j++) {
            long long required_time = 0;
            // Calculate max time for task j
            for (int i = 0; i < n; i++) {
                long long remaining_skill = prefix_sum[n-1] - (i > 0 ? prefix_sum[i-1] : 0);
                long long next_finish_time = finish_times[i] + remaining_skill * mana[j];
                required_time = max(required_time, next_finish_time);
            }
            
            // Update finish time for the last worker
            finish_times[n-1] = max(finish_times[n-1], required_time);
            
            // Backpropagate finish times
            for (int i = n-2; i >= 0; i--) {
                finish_times[i] = finish_times[i+1] - skill[i+1] * mana[j];
            }
        }
        return finish_times[n-1];
    }
};