# Intuition

當n的範圍拉高到10^9後, 遍歷整個n就會超時了, 這時根據新的數據範圍可以:

Key Optimizations:

1. Matrix Exponentiation: The DP transition is linear, so we can represent it as a matrix multiplication. Instead of iterating n times, we compute matrix^(n-1) using binary exponentiation in O(log n) time.
2. State Representation: The state vector contains all dp0[0..r] and dp1[0..r] values (total size: 2*(r-l+1)).
3. Transition Matrix:

next_dp1[num] = sum(dp0[j] for j < num)
next_dp0[num] = sum(dp1[j] for j > num)


4. i-k-j loop ordering in matrix multiplication: This has much better cache locality and skips zeros early
5. Binary exponentiation: O(log n) matrix multiplications instead of O(n)
6. Early zero-checking: Skips multiplication when A[i][k] == 0

This approach works because with the new constraints, r - l ≤ 74 is small enough that matrix operations are efficient, while log(10^9) ≈ 30 makes the number of iterations manageable!

[video explanation](https://www.youtube.com/watch?v=bhMq96VOfAk)

概念上像這樣 (從Number of ZigZag Arrays I)衍伸過來:

```py
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        
        # Build transition matrix
        # State: [dp0[0], dp0[1], ..., dp0[r], dp1[0], dp1[1], ..., dp1[r]]
        # Total size: 2 * (r+1)
        size = r - l + 1
        matrix_size = 2 * size
        transition = [[0] * matrix_size for _ in range(matrix_size)]
        
        # Fill transition matrix based on the recurrence relations
        # next_dp1[num] = sum(dp0[j] for j < num)
        # next_dp0[num] = sum(dp1[j] for j > num)
        
        for num in range(size):
            # next_dp1[num] depends on dp0[0..num-1]
            for j in range(num):
                transition[size + num][j] = 1
            
            # next_dp0[num] depends on dp1[num+1..r]
            for j in range(num + 1, size):
                transition[num][size + j] = 1
        
        # Initial state: all dp0 and dp1 are 1
        state = [1] * matrix_size
        
        # Apply matrix exponentiation (n-1) times
        result_state = self.matrix_power_multiply(transition, state, n - 1, mod)
        
        # Sum all values
        return sum(result_state) % mod
    
    def matrix_multiply(self, A, B, mod):
        """Multiply two matrices A and B"""
        n = len(A)
        m = len(B[0])
        k = len(B)
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for p in range(k):
                    result[i][j] = (result[i][j] + A[i][p] * B[p][j]) % mod
        return result
    
    def matrix_power(self, matrix, exp, mod):
        """Compute matrix^exp using binary exponentiation"""
        n = len(matrix)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        base = [row[:] for row in matrix]
        
        while exp > 0:
            if exp % 2 == 1:
                result = self.matrix_multiply(result, base, mod)
            base = self.matrix_multiply(base, base, mod)
            exp //= 2
        
        return result
    
    def matrix_power_multiply(self, matrix, vector, exp, mod):
        """Compute (matrix^exp) * vector efficiently"""
        if exp == 0:
            return vector
        
        # Compute matrix^exp
        powered_matrix = self.matrix_power(matrix, exp, mod)
        
        # Multiply by vector
        n = len(vector)
        result = [0] * n
        for i in range(n):
            for j in range(n):
                result[i] = (result[i] + powered_matrix[i][j] * vector[j]) % mod
        
        return result
```

但這樣會TLE在最後個test case, 所以還得優化一下

# Complexity:

Time: O((r-l)³ × log n) ≈ O(75³ × 30) ≈ O(13M) operations - easily fits in time limit
Space: O((r-l)²) ≈ O(5625)

