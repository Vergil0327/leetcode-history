class Solution:
    """
    Since $arr[i]$ is limited to $[0, 5000]$, and the number of elements $n$ is up to $1000$, we can use Dynamic Programming.
    State: dp[i][last_val] = number of valid non-decreasing subarrays from index $i$ to $n-1$, given that the previous element was last_val.
    Preprocessing: Create a list valid_numbers[s] containing all integers $v \in [0, 5000]$ such that the sum of digits of $v$ equals $s$.
    Transitions: To compute dp[i][last_val], we iterate through all $v$ in valid_numbers[digitSum[i]]. If $v \ge last\_val$, we add dp[i+1][v] to our total.
    Optimization: Summing up dp[i+1][v] for all $v \ge last\_val$ can be done in $O(1)$ using Suffix Sums to avoid $O(5000^2)$ complexity.

    Complexity Analysis
    Preprocessing: $O(5000 \cdot \text{digits}) \approx 20,000$ operations.
    DP: $O(N \cdot \text{MAX\_VAL})$. With $N=1000$ and $MAX\_VAL=5000$, this is $5 \times 10^6$ operations. This fits comfortably within the 2-second time limit for Python.
    Space: $O(\text{MAX\_VAL})$ to store the DP table and the suffix sums.
    """
    def countArrays(self, digitSum: list[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 5000
        
        # 1. Pre-group numbers by their digit sums
        # valid_nums[s] = [v1, v2, ...] where sum_digits(v) == s
        valid_nums = [[] for _ in range(51)]
        for v in range(MAX_VAL + 1):
            s = sum(int(d) for d in str(v))
            if s <= 50:
                valid_nums[s].append(v)
        
        n = len(digitSum)
        
        # 2. DP initialization
        # dp[v] will store the number of ways to complete the array 
        # starting from the current index if the previous value was v.
        # We start from the last element and move backwards.
        
        # Base case: For the last element, any v >= prev_v is 1 way
        # Initialize dp for the "after the last" index
        dp = [1] * (MAX_VAL + 2) 
        
        for i in range(n - 1, -1, -1):
            s = digitSum[i]
            current_targets = valid_nums[s]
            
            # new_dp[v] will be the number of ways if the PREVIOUS element was v
            new_dp = [0] * (MAX_VAL + 2)
            
            # Suffix sums of the PREVIOUS dp table to get O(1) transitions
            # suffix[v] = sum(dp[x] for x in target_vals if x >= v)
            # This is tricky because dp[x] only matters if x is a valid target for index i
            
            # Step A: Calculate contribution of valid numbers for THIS index
            contributions = [0] * (MAX_VAL + 2)
            for v in current_targets:
                # ways to continue from v = dp[v] (from the i+1 iteration)
                contributions[v] = dp[v]
            
            # Step B: Build suffix sum of contributions
            suffix_sum = 0
            for v in range(MAX_VAL, -1, -1):
                suffix_sum = (suffix_sum + contributions[v]) % MOD
                new_dp[v] = suffix_sum
            
            dp = new_dp
            
        # The answer is dp[0] (meaning previous value was 0 or less)
        return dp[0]