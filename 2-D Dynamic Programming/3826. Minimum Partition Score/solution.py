from itertools import accumulate


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Precompute prefix sums for O(1) subarray sum calculation
        prefix_sum = list(accumulate(nums, initial=0))
            
        def get_value(s):
            return s * (s + 1) // 2
        
        # dp[i] will store the min score for the current number of partitions
        # Initialize with infinity
        dp = [float('inf')] * (n + 1)
        
        # Base case:
        for j in range(1, n + 1):
            dp[j] = get_value(prefix_sum[j])
            
        # Iterate for partitions from 2 to k
        for i in range(2, k + 1):
            new_dp = [float('inf')] * (n + 1)
            # Optimization: split point p must be at least i-1
            # We can use a simple loop here for N=1000, 
            # or optimize further with Divide and Conquer DP optimization.
            
            # Divide and Conquer Optimization function
            def compute(l, r, optL, optR):
                if l > r: return
                
                mid = (l + r) // 2
                best_p = -1
                
                # The split point p must leave enough elements for i-1 partitions
                # and cannot exceed mid-1
                for p in range(max(i - 1, optL), min(mid, optR + 1)):
                    current_val = dp[p] + get_value(prefix_sum[mid] - prefix_sum[p])
                    if current_val < new_dp[mid]:
                        new_dp[mid] = current_val
                        best_p = p
                
                compute(l, mid - 1, optL, best_p)
                compute(mid + 1, r, best_p, optR)

            # The reason for choosing the range (i, n, i-1, n-1) for the initial call to compute(l, r, optL, optR) is based on the physical boundaries of the partitioning problem and the structure of your DP table.1.
            
            # The Range of l and r (i to n)
            # The parameters l and r represent the indices of nums for which we are currently calculating the minimum score.
            #     Start at i: If we want to partition the array into i subarrays, we need at least i elements. It is impossible to partition 2 elements into 3 subarrays, so we start our calculation from the $i$-th element.
            #     End at n: We need to calculate the DP value for all possible lengths of the array, up to the full length $n$.2.
            
            # The Range of optL and optR (i-1 to n-1)
            # The parameters optL and optR define the search space for the "split point" $p$ that separates the $(i-1)$-th subarray from the $i$-th (last) subarray.
            #     optL = i-1: To have $i$ subarrays, the first $i-1$ subarrays must contain at least $i-1$ elements total. Therefore, the split point $p$ (which is the end of the $(i-1)$-th subarray) cannot be smaller than $i-1$.
            #     optR = n-1: The split point $p$ must leave at least one element for the $i$-th subarray. Since the maximum index we consider for the whole partition is $n$, the furthest the previous partition can end is $n-1$.3.
            
            # Visualizing the Split
            # Think of the partition as a cut at index $p$:[Subarrays 1 to i-1] | [Subarray i]
            #     The left side must have at least $i-1$ elements to satisfy the $k$ partitions requirement.
            #     The right side must have at least $1$ element.
            #     The range of $p$ is therefore constrained between the minimum elements needed on the left ($i-1$) and the maximum elements available before the last one ($n-1$).
            compute(i, n, i - 1, n - 1)
            dp = new_dp
            
        return dp[n]