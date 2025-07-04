class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        long long size = 1;
        int total_op = 0;
        while (size < k) {
            total_op++;
            size *= 2;
        }

        int shift = 0;
        for (int i=total_op-1; i>=0; i--) {
            if (k > size/2) /* from shift&append operation */ {
                if (operations[i] == 1) /* shift&append */ {
                    shift++;
                    k -= size/2;
                } else /* copy */ {
                    k -= size/2;
                }
            }
            size /= 2;
        }
        return 'a' + (shift%26);
    }
};