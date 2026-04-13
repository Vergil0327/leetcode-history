import math

class Solution:
    """
    Why this works (The Intuition)
    The Filter: Any subsequence with GCD $p$ must consist entirely of multiples of $p$. By setting non-multiples to 0 in our tree, we effectively ignore them, because $gcd(x, 0) = x$.
    The Root: tree[1] always stores the GCD of all "eligible" numbers currently in the array. If tree[1] == p, we know at least one subsequence has GCD $p$ (the one containing all eligible numbers).
    The "Proper Subsequence" Trap: The problem says the subsequence must be strictly less than length $n$.
        - If some numbers in the array are not multiples of $p$, then our "eligible" set is already smaller than $n$. We win.
        - If every number is a multiple of $p$, we have to see if we can kick one out and still keep the GCD at $p$.
        
    Complexity
    Time: Each query takes $O(\log n \cdot \log(\max(\text{nums})))$ to update the tree. The brute force for small $n$ is $O(n^2)$, but only runs when $n \le 6$, so it's effectively constant time.
    Space: $O(n)$ to store the Segment Tree.

    1. The Mathematical Trap

    As you saw in the failing test case, it is possible to have an array where:
    - The GCD of all $n$ elements is 1.
    - The GCD of any $n-1$ elements is greater than 1.
    
    This only happens when each element in the set is "missing" exactly one prime factor that all other elements share. For this to happen, you need a distinct prime for every single index.
        - To block 2 indices, you need 2 primes (e.g., $\{3, 2\}$).
        - To block 6 indices, you need 6 primes ($2, 3, 5, 7, 11, 13$). The product of these first six primes is 30,030.
        - To block 7 indices, you would need the 7th prime (17). $30,030 \times 17 = \mathbf{510,510}$.2.
        
    Why "6"?The constraints of the problem state that nums[i] cannot exceed 50,000. A number can only be a "perfectly blocked" member of a set of size 7 if it is a multiple of at least 6 distinct primes.As shown above, the smallest number that is a multiple of the first 6 primes is $30,030$.The smallest number that is a multiple of 7 distinct primes is $510,510$, which is way above the 50,000 limit.Therefore, it is physically impossible to create a "perfectly blocked" set of size 7 or larger within the given constraints. If $n > 6$ and the total GCD is $p$, there must be a proper subsequence with GCD $p$.3. Summary of the LogicIf $n > 6$: The numbers aren't large enough to "trap" you. If the total GCD is $p$, a proper subsequence is guaranteed.If $n \le 6$: The numbers are small enough that you could be trapped (like the $15015$ case where $n=6$). We run a quick brute-force check just to be safe.
    """
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        n = len(nums)
        # 1. Initialize the Segment Tree size to a power of 2
        size = 1
        while size < n:
            size *= 2
        tree = [0] * (2 * size)
        
        # 2. Count of elements divisible by p (candidates for a subseq)
        cnt_p = 0

        def update_tree(idx, val):
            nonlocal cnt_p
            # Update count if eligibility changed
            was_p = (nums[idx] % p == 0)
            is_p = (val % p == 0)
            if was_p and not is_p: cnt_p -= 1
            if not was_p and is_p: cnt_p += 1
            
            nums[idx] = val
            # Update leaf: Only store in tree if it's a multiple of p
            pos = size + idx
            tree[pos] = val if is_p else 0
            
            # 3. Bubble up the GCD change to the root
            pos //= 2
            while pos >= 1:
                tree[pos] = math.gcd(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        # Initial build
        for i in range(n):
            val = nums[i]
            if val % p == 0:
                cnt_p += 1
                tree[size + i] = val
        
        for i in range(size - 1, 0, -1):
            tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])

        ans = 0
        for idx, val in queries:
            update_tree(idx, val)
            
            # Root of the tree (tree[1]) is the GCD of all multiples of p
            if tree[1] == p:
                if cnt_p < n:
                    # If we aren't using the whole array, any subseq with GCD p works
                    ans += 1
                else:
                    # If using all elements, we must check if a proper subseq exists
                    # For n > 6, it is mathematically guaranteed if GCD=p
                    # 2*3*5*7*11*13 = 30030, for nums[i] <= 10^5, once n > 6, which means minimum valid subsequence[2,3,5,7,11,13] is guaranteed.
                    if n > 6:
                        ans += 1
                    else:
                        # For very small n, brute force check by dropping one element at a time
                        if self.can_drop_one(nums, n, p):
                            ans += 1
        return ans

    def can_drop_one(self, nums, n, p):
        for i in range(n):
            current_gcd = 0
            for j in range(n):
                if i == j: continue
                current_gcd = math.gcd(current_gcd, nums[j])
            if current_gcd == p:
                return True
        return False