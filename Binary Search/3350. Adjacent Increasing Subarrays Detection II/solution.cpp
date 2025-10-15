/**
2 cases:
    1. one increasing subarray: k = length / 2
    2. two adjacent subarray: k = min(length1, length2) ex. X X X X X X X {X X X} {Y Y Y}
*/
class Solution {
    
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        
        int ans = 1;
        int prev = 0;
        int length = 1;
        for(int i = 1; i < n; i++) {
            if(nums[i - 1] < nums[i]) {
                length++;
            } else {
                prev = length;
                length = 1;
            }
            ans = max(ans, max(length / 2, min(length, prev)));
        }
            
       
        return ans;

    }
};