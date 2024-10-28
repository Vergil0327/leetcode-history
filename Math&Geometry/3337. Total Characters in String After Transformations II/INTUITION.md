# Intuition

每個character間的轉換有點graph的感覺, nums[i]告訴我們節點`i`的dependencies:

i 連結到 i+1, i+2, i+3, ..., i+nums[i]

可以很自然寫出`O(t * 26 * max(nums))`的dp solution

```py
def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
    mod = 10**9 + 7
    
    dp = [0] * 26
    for ch in s:
        dp[ord(ch)-ord("a")] += 1

    for _ in range(t):
        new_dp = [0]*26
        for ch in range(26):
            for j in range(1, nums[ch]+1):
                new_dp[(ch+j)%26] = (new_dp[(ch+j)%26] + dp[ch]) % mod
        dp = new_dp
    return sum(dp) % mod
```

但由於t <= 10^9, O(t)肯定會TLE

由於沒有其他地方能下手, 也想不到優化的地方, 這題就這麼卡住
看了提示才發現需要利用到數學的矩陣運算來加速運算

數學不是強項
這邊直接提供大神@lee215的解法

```py
class Solution:
    def mat_pow(self, matrix, n, mod):
        size = len(matrix)
        res = [[int(i == j) for j in range(size)] for i in range(size)]

        while n > 0:
            if n & 1:
                res = self.mat_mul(res, matrix, mod)
            matrix = self.mat_mul(matrix, matrix, mod)
            
            n //= 2
        return res

    def mat_mul(self, mat1, mat2, mod):
        """
        mat1      mat2
        X X X     O O O
        X X X  *  O O O = 
        X X X     O O O

        1-indexed來看的話:
        res[1][1] = sum(row1 of mat1 * col1 of mat2)
        """
        res = [[0]*len(mat2[0]) for _ in range(len(mat1))]

        for r in range(len(mat1)):
            for c in range(len(mat2[0])):
                for k in range(len(mat2)):
                    res[r][c] += mat1[r][k] * mat2[k][c]
                res[r][c] %= mod
        return res


    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7

        adjacency_list = [[0] * 26 for _ in range(26)]
        for i, num in enumerate(nums):
            for j in range(i+1, i+num+1):
                adjacency_list[i][j%26] = 1

        mat = self.mat_pow(adjacency_list, t, mod)

        count = [0] * 26
        for ch in s:
            count[ord(ch)-ord("a")] += 1
        res = self.mat_mul([count], mat, mod)

        return sum(res[0]) % mod
```

並提供思路解析

Explanation of Key Steps
1. Matrix Exponentiation (mat_pow function):
   - Matrix exponentiation is used to compute the effect of t transformations efficiently.
   - The mat_pow function implements the "exponentiation by squaring" technique, which allows us to raise a matrix to a power in O(log t) time, improving performance for large t.

2. Matrix Multiplication (mat_mul function):
   - This function performs matrix multiplication of two matrices and takes modulo mod for each element to prevent overflow.
   - It multiplies each row of the first matrix (mat1) by each column of the second matrix (mat2) to produce the result matrix.

3. Building the Adjacency Matrix:
   - The adjacency matrix (adjacency_list) represents the transformations for each character.
   - For each character represented by index i, we mark the next nums[i] positions (with wrap-around) in the matrix as reachable in a single transformation.
   - if adjacency_list[i][j] = 1, it means after **one** transformation, char `i` can generate one `j`

4. Counting Initial Characters:
   - We create a count array to store the initial counts of each character in s.
   - This allows us to determine the initial distribution of characters before any transformations.

5. Applying the Transformation Matrix:
   - We multiply the initial character count vector with the transformation matrix raised to the power t.
   - This results in the final distribution of characters after t transformations.

6. Returning the Final Result:
   - The sum of the transformed counts gives the final length of the resulting string, which is returned modulo `10**9 + 7`. This sum represents the total number of characters in the transformed string after exactly t transformations.

This approach efficiently handles large values of t and leverages matrix exponentiation and multiplication to simulate transformations over multiple steps. The use of modular arithmetic ensures that the result remains manageable, even for large inputs.

## Intuition Behind Using Matrix Multiplication for This Problem

To understand why matrix multiplication is useful for this problem, let’s break down the requirements and the reasoning for modeling it this way.

### Problem Breakdown and Intuition

The problem involves a series of transformations where each character in the string can change to a set of consecutive characters in the alphabet. The transformations repeat `t` times, and for each character, its transformation is based on a given rule defined by the array `nums`. Each transformation step causes each character to potentially expand into multiple characters, following the wrap-around rule of the alphabet.

1. **Transformations as Transitions**:
   - Each character transformation (like changing `'a'` to `'bcd'`) can be seen as a transition from one character state to multiple character states.
   - If we imagine each character (from `'a'` to `'z'`) as a "state," then transforming a character repeatedly through multiple steps is analogous to state transitions in a system.

2. **Tracking Character Count Growth**:
   - At each step, a character might "expand" into multiple other characters, increasing the total length of the string.
   - After each transformation, we want to know the total count of each character in the string to calculate the length of the transformed string.

3. **Adjacency Matrix Representation**:
   - The adjacency matrix, `adjacency_list`, represents which characters each character can transition to in a single transformation.
   - `adjacency_list[i][j] = 1` means that in a single transformation, character `i` (e.g., `'a'`) can expand to include character `j` (e.g., `'b'`, `'c'`, etc.), according to the transformation rules.

4. **Why Matrix Multiplication Works**:
   - Matrix multiplication allows us to compute the cumulative effect of these transformations over multiple steps.
   - If we multiply the initial count of characters by the transformation matrix, the resulting vector tells us the count of each character after a single transformation.
   - By raising the transformation matrix to the power `t` (using matrix exponentiation), we can apply the transformation `t` times in one go.
   - Each matrix exponentiation step simulates a "step" in our transformation process, so multiplying the matrix `t` times allows us to get the result after `t` transformations directly.

5. **How Matrix Multiplication Models the Problem**:
   - Imagine each row of the adjacency matrix as the "transformation rule" for a particular character.
   - When you multiply this adjacency matrix by a vector representing character counts, you get the new counts of characters after one transformation.
   - For example:
     - If initially, we have one `'a'`, and `'a'` transforms to `'bcd'`, then the matrix multiplication will propagate this transformation across multiple steps.
   - Using matrix exponentiation, we can compute the transformation matrix raised to the power `t` (representing `t` transformations), and multiplying this result by the initial character counts gives the final distribution.

### Why Matrix Multiplication is Efficient Here

Matrix multiplication and matrix exponentiation allow us to handle exponential growth (like this character expansion) efficiently:
   - Directly performing `t` transformations would be slow, as the length of the string can grow rapidly.
   - By using matrix exponentiation, we simulate the result of `t` transformations in `O(log t)` matrix multiplications, which is much faster.

### Summary

In summary, matrix multiplication is an efficient way to model cumulative transformations where each transformation depends linearly on previous results. Here, it allows us to capture the essence of character expansion across multiple transformations and directly calculate the final result after `t` transformations without actually expanding the string step-by-step.

# Complexity

## Time Complexity

1. Constructing adjacency_list: O(26*26) = O(1) for fixed-size matrix
2. mat_pow for O(log(t)), each matrix multiplication for O(26^3)
   - overall: O(log(t) * 26^3)
3. Matrix Multiplication: O(26^3)

therefore, O(log(t))

## Space Complexity

O(26*26) = O(1) space