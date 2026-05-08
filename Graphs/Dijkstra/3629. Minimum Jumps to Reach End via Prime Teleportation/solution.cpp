#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <map>

using namespace std;
using LL = long long;
using vll = vector<LL>;

class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        map<int, vector<int>> teleport;
        for (int i=0; i<n; i++) {
            int p = 2, num = nums[i];
            while (p * p <= num) {
                if (num%p == 0) {
                    teleport[p].push_back(i);
                    while (num%p == 0) {
                        num /= p;
                    }
                }
                p++;
            }
            if (num > 1) {
                teleport[num].push_back(i);
            }
        }

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        pq.push({0, 0}); // step, position

        vector<int> distance(n, 1e9);
        distance[0] = 0;
        while (!pq.empty()) {
            auto item = pq.top();
            pq.pop();

            int step = item[0], pos = item[1];
            if (step > distance[pos]) continue;

            if (pos-1 >= 0 && step+1 < distance[pos-1]) {
                // update backwards
                distance[pos-1] = step+1;
                pq.push({step+1, pos-1});
            }
            
            if (pos+1 < n && step+1 < distance[pos+1]) {
                // update backwards
                distance[pos+1] = step+1;
                pq.push({step+1, pos+1});
            }

            if (teleport.find(nums[pos]) != teleport.end()) {
                // update teleport
                for (const auto& nxt : teleport[nums[pos]]) {
                    if (nxt != pos && step+1 < distance[nxt]) {
                        distance[nxt] = step+1;
                        pq.push({step+1, nxt});
                    }
                }
                
                teleport.erase(nums[pos]); // prune
            }
        }

        return distance[n-1];
    }
};