"""
### Optimal 0/1 Knapsack DP Strategy

Since n <= 1000 and s <= 1000:
1. Generate all primes <= n using Sieve of Eratosthenes up to n (inclusive).
2. Use 0/1 Knapsack DP where dp[w] stores (min_elements) for sum w.
3. Find the maximum achievable sum `max_sum` (1 <= max_sum <= s) that uses at least 1 element and minimizes element count.
4. To greedily construct the lexicographically smallest subset:
    1. Process prime candidates `p = primes[i]` from smallest (`i = 0`) to largest.
    2. At index `i`, pick `primes[i]` IF `curr_w >= p` AND the remaining `(num_primes - 1 - i)` primes can form the remaining sum `curr_w - p` using `curr_count - 1` elements.
    3. We compute a suffix DP `suffix_memo[i][w]` = min elements needed to get sum `w` using a subset of `primes[i...]`.

=== COMPLEXITY ANALYSIS ===

1. Time Complexity:
   - Sieve: O(N log log N)
   - Knapsack DP: O(P * S) where P is the number of primes <= N (P <= 168 for N=1000) and S <= 1000.
     Total operations: ~168 * 1000 = 1.68 * 10^5 operations (well within 1-second limit).
   - Reconstruction: O(P)
   - Total Time Complexity: O(P * S) = O(N/log N * S)

2. Space Complexity:
   - DP table: O(P * S) to store memo state for exact tie-breaking reconstruction.
   - Total Space Complexity: O(N * S / log N)


=== WHY SUFFIX DP WORKS ===

1. Suffix DP `suffix_dp[i][w]` calculates the min elements needed using primes from index i to P-1.
2. In Step 4, as we iterate from i = 0 to P-1, we consider primes in strictly ascending order.
3. At index i, checking `suffix_dp[i + 1][curr_w - p] == curr_count - 1` determines whether taking prime `primes[i]` allows completing the exact target sum with the required minimum count using the remaining primes.
4. Taking `primes[i]` at the earliest possible index guarantees the lexicographically smallest list.
"""

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        # Step 1: Generate primes <= n
        isPrime = [True] * (n + 1)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
        primes = [i for i in range(2, n + 1) if isPrime[i]]
        
        if not primes or s < primes[0]:
            return []

        P = len(primes)
        INF = float('inf')

        # Step 2: Suffix DP
        # suffix_dp[i][w] = min elements needed to form sum w using a subset of primes[i:]
        suffix_dp = [[INF] * (s + 1) for _ in range(P + 1)]
        suffix_dp[P][0] = 0

        for i in range(P - 1, -1, -1):
            p = primes[i]
            for w in range(s + 1):
                suffix_dp[i][w] = suffix_dp[i + 1][w]
                if w >= p and suffix_dp[i + 1][w - p] != INF:
                    suffix_dp[i][w] = min(suffix_dp[i][w], suffix_dp[i + 1][w - p] + 1)

        # Step 3: Find best total sum <= s (must be non-empty, i.e., sum > 0)
        best_sum = -1
        min_count = INF

        for w in range(1, s + 1):
            count = suffix_dp[0][w]
            if count != INF:
                if w > best_sum:
                    best_sum = w
                    min_count = count
                elif w == best_sum and count < min_count:
                    min_count = count

        if best_sum == -1:
            return []

        # Step 4: Forward Reconstruction (Greedy lexicographical choice)
        res = []
        curr_w = best_sum
        curr_count = min_count

        for i in range(P):
            p = primes[i]
            # Try to pick primes[i]:
            # If picking p is valid and leads to a valid suffix solution for the remaining targets
            if curr_w >= p and suffix_dp[i + 1][curr_w - p] == curr_count - 1:
                res.append(p)
                curr_w -= p
                curr_count -= 1

        return res