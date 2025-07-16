using pii = pair<int, int>;

class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        if (k > n || n == 0 || k == 0) return 0;

        vector<pair<int,int>> pairs;
        for (int i=0; i<n; i++) {
            pairs.push_back({nums2[i], nums1[i]});
        }

        sort(pairs.begin(), pairs.end(), greater{});

        long long sum=0;
        priority_queue<int, vector<int>, greater<int>> min_heap;
        for (int i=0; i<k; i++) {
            sum += pairs[i].second;
            min_heap.push(pairs[i].second);
        }
        long long res = pairs[k-1].first * sum;

        for (int i=k; i<n; i++) {
            min_heap.push(pairs[i].second);
            sum += pairs[i].second;

            sum -= min_heap.top();
            min_heap.pop();

            res = max(res, pairs[i].first * sum);
        }
        return res;
    }
};
