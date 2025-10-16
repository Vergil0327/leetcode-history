class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        int n = nums.size();
        unordered_map<int,int> m;
        for (int i=0; i<n; i++) {
            int x = ((nums[i]%value)+value)%value;
            m[x]++;
        }

        int MEX = 0;
        while (m.count(MEX) && m[MEX] > 0) {
            m[MEX] -= 1;
            int x = 1;
            while (m[MEX] > 0) {
                while (m.count(MEX+value*x)) x++;
                m[MEX+value*x]++;
                m[MEX]--;
            }
            MEX++;
        }
        return MEX;
    }
};

class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        vector<int> rems(value + 1, 0);
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] >= 0)
                ++rems[nums[i] % value];
            else
                ++rems[value + (nums[i] % value)];
        }
        rems[0] += rems[value];

        int ret = 0;
        while(rems[ret % value]-- > 0)
            ++ret;
        return ret;
    }
};