using pll = pair<long long, long long>;
using LL = long long;
class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();

        vector<LL> res(n-k+1, 0);
        
        unordered_map<LL, LL> count;
        for (int i=0; i<k-1; i++) {
            count[nums[i]]++;
        }

        unordered_set<LL> s;
        for (auto& num : nums) {
            s.insert(num);
        }

        auto cmp = [](const pll& a, const pll& b) {
            if (a.first != b.first) return a.first > b.first;  // Descending count
            return a.second > b.second;  // Descending value
        };
        set<pll, decltype(cmp)> topX(cmp), rest(cmp);
        for (const auto& num : s) {
            rest.insert({count[num], num});
        }
        
        LL sumX = 0;
        // When moving from rest to topX: take the largest (begin)
        while (!rest.empty() && topX.size() < x) {
            auto iter = rest.begin();  // Largest element
            auto item = *iter;
            sumX += item.first * item.second;
            rest.erase(iter);
            topX.insert(item);
        }

        for (int i=k-1; i<n; i++) {
            // add i-th item to sliding window
            pll old = {count[nums[i]], nums[i]};
            if (topX.count(old)) {
                sumX -= old.first * old.second;
                topX.erase(old);
            } else {
                rest.erase(old);
            }

            count[nums[i]]++;

            pll new_item = {count[nums[i]], nums[i]};
            topX.insert(new_item);
            sumX += new_item.first * new_item.second;

            // When removing from topX: remove the smallest (end()--)
            while (!topX.empty() && topX.size() > x) {
                auto iter = topX.end();
                iter--;  // Smallest element
                auto item = *iter;
                sumX -= item.first * item.second;
                topX.erase(iter);
                rest.insert(item);
            }

            res[i-k+1] = sumX;
            
            // remove leftmost item in sliding window
            pll leftmost = {count[nums[i-k+1]], nums[i-k+1]};
            if (topX.count(leftmost)) {
                sumX -= leftmost.first * leftmost.second;
                topX.erase(leftmost);
            } else {
                rest.erase(leftmost);
            }

            count[nums[i-k+1]]--;
            rest.insert({count[nums[i-k+1]], nums[i-k+1]});

            // When moving from rest to topX: take the largest (begin)
            while (!rest.empty() && topX.size() < x) {
                auto iter = rest.begin();  // Largest element
                auto item = *iter;
                sumX += item.first * item.second;
                rest.erase(iter);
                topX.insert(item);
            }
        }

        return res;
    }
};