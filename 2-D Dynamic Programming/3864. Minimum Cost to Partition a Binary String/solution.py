import functools
class Solution:
    """
    State Space Reduction: By using (l, length) instead of (l, r), the hashing and storage become slightly more predictable for the Python interpreter.
    lru_cache: It is implemented in C and is generally more memory-efficient than a standard Python dictionary for storing recursion results.
    Avoids Redundant Calculations: Because the splits are always powers of 2 (relative to the original length or its odd factors), the number of (l, length) pairs is strictly limited to $O(N)$.
    """
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (1 if s[i] == '1' else 0)

        # Using lru_cache is often more memory-efficient than a manual dict for 
        # recursion, but the real key is limiting the state space.
        @functools.lru_cache(None)
        def solve(l, length):
            r = l + length - 1
            num_ones = prefix_ones[r + 1] - prefix_ones[l]
            
            # Base cost for this segment
            current_cost = flatCost if num_ones == 0 else length * num_ones * encCost
            
            # If we can't split, return base cost
            if length % 2 != 0: return current_cost
            
            # Try splitting
            half = length // 2
            split_cost = solve(l, half) + solve(l + half, half)
            
            return min(current_cost, split_cost)

        return solve(0, n)
    

# If it still fails:
# We can use an Iterative Bottom-Up approach. This is the most memory-stable way:
class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (1 if s[i] == '1' else 0)

        # Identify all lengths that will be generated (n, n/2, n/4...)
        lengths = []
        curr = n
        while curr > 0:
            lengths.append(curr)
            if curr % 2 != 0: break
            curr //= 2
        
        # Bottom-up: solve for smallest lengths first
        dp = {} # (start_index, length) -> cost
        for length in reversed(lengths):
            for l in range(0, n, length):
                if l + length > n: continue
                
                num_ones = prefix_ones[l + length] - prefix_ones[l]
                base_cost = flatCost if num_ones == 0 else length * num_ones * encCost
                
                if length % 2 != 0:
                    dp[(l, length)] = base_cost
                else:
                    half = length // 2
                    # The halves were already computed in the previous iteration
                    split_cost = dp[(l, half)] + dp[(l + half, half)]
                    dp[(l, length)] = min(base_cost, split_cost)
                    
        return dp[(0, n)]