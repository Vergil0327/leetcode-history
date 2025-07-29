// Intuition: OR 這操作只會越來越大, 所以從後往前遍歷的話, 對於當前的nums[i:]來說, 當下的OR(nums[i:])就是 maximum OR

// solution 1: sliding window
class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);

        int r = n-1;
        vector<int> bits(32, 0);
        for (int l=n-1; l>=0; l--) {
            for (int j=0; j<32; j++) {
                if ((nums[l]>>j)&1) {
                    bits[j]++;
                }
            }

            while (l < r) {
                vector<int> next(32, 0);
                copy(bits.begin(), bits.end(), next.begin());
                bool same = true;
                for (int j=0; j<32; j++) {
                    if ((nums[r]>>j)&1) {
                        next[j]--;
                        if (next[j] == 0) {
                            same = false;
                            break;
                        }
                    }
                }

                if (same) {
                    r--;
                    bits = next;
                } else {
                    break;
                }
            }
            res[l] = r-l+1;
        }
        return res;
    }
};

// solution 2: record each bit's position. the right-most position is the right boundary we must have.
class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        vector<int> nextbit(32,-1);
        vector<int> ans(nums.size());
        for (int i=nums.size()-1; i>=0; i--) {
            int curr=nums[i];
            for(int j=0;j<32;j++) {
                if ((nums[i]>>j)&1) {
                    nextbit[j] = i;
                }
            }

            int maxi=-1;
            for(int j=0;j<32;j++) {
                maxi=max(maxi, nextbit[j]);
            }

            ans[i] = max(1, maxi-i+1); // 1 element at least. if nums[i] equals 0, maxi will be -1.
        }
        return ans;
    }
};