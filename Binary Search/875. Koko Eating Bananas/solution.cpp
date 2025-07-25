class Solution {
public:
    int check(vector<int>& piles, int h, int k) {
        for (auto& num : piles) {
            h -= (num+k-1)/k; // ceil(num/k)
        }
        return h >= 0;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int l=1, r=*max_element(piles.begin(), piles.end());

        while (l < r) {
            int mid = l + (r-l)/2;

            if (check(piles, h, mid)) {
                r = mid;
            } else {
                l = mid+1;
            }
        }
        return l;
    }
};