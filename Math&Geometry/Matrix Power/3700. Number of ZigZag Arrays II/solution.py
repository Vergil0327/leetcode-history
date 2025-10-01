class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        size = r - l + 1
        
        if n == 1:
            return (2 * size) % mod
        
        # Build transition matrix
        M = self.build_matrix(size)
        
        # Initial state: all 1s
        state = [1] * (2 * size)
        
        # Compute M^(n-1) * state using matrix exponentiation
        result = self.mat_pow_mul(M, state, n - 1, mod)
        
        return sum(result) % mod
    
    def build_matrix(self, size):
        """Build the 2*size x 2*size transition matrix"""
        n = 2 * size
        M = [[0] * n for _ in range(n)]
        
        # next_dp0[i] = sum(dp1[j] for j > i)
        for i in range(size):
            for j in range(i + 1, size):
                M[i][size + j] = 1
        
        # next_dp1[i] = sum(dp0[j] for j < i)
        for i in range(size):
            for j in range(i):
                M[size + i][j] = 1
        
        return M
    
    def mat_mul(self, A, B, mod):
        """Optimized matrix multiplication with i-k-j ordering"""
        n = len(A)
        C = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for k in range(n):
                if A[i][k]:  # Skip if zero
                    Aik = A[i][k]
                    for j in range(n):
                        C[i][j] = (C[i][j] + Aik * B[k][j]) % mod
        
        return C
    
    def mat_pow(self, M, exp, mod):
        """Matrix exponentiation using binary exponentiation"""
        n = len(M)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        base = [row[:] for row in M]
        
        while exp > 0:
            if exp & 1:
                result = self.mat_mul(result, base, mod)
            base = self.mat_mul(base, base, mod)
            exp >>= 1
        
        return result
    
    def mat_pow_mul(self, M, v, exp, mod):
        """Compute (M^exp) * v efficiently"""
        if exp == 0:
            return v
        
        # Compute M^exp
        M_exp = self.mat_pow(M, exp, mod)
        
        # Multiply by vector
        n = len(v)
        result = [0] * n
        for i in range(n):
            for j in range(n):
                result[i] = (result[i] + M_exp[i][j] * v[j]) % mod
        
        return result