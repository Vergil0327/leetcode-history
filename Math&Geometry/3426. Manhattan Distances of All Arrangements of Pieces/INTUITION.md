# Intuition

1. Manhattan Distance Decomposition:
   - The Manhattan distance between two points (𝑥1,𝑦1) and (𝑥2,𝑦2) is: ∣𝑥1−𝑥2∣+∣𝑦1−𝑦2∣
   - This distance can be split into contributions from the x-axis difference (∣𝑥1−𝑥2∣) and the y-axis difference  (∣𝑦1−𝑦2∣).

2. Symmetry and Pairwise Distances:
   - Since the 𝑘 pieces are identical and indistinguishable, we only care about the sum of Manhattan distances between all pairs of pieces, regardless of the specific arrangement of pieces.

3. Number of Valid Arrangements:

- The grid has 𝑚×𝑛 cells, and 𝑘 pieces are placed with at most one piece per cell.
- If two pieces are fixed, the remaining 𝑘−2 pieces can be placed in C(𝑚⋅𝑛−2, 𝑘−2) ways. This count is constant across all arrangements.

4. Modular Arithmetic: Since the result can be very large, modular arithmetic ensures we return the result modulo $10^9+7$

# Approach

### Compute the Base Factor:

Fix two pieces at any two cells. The remaining 𝑘−2 pieces can be placed in C(𝑚⋅𝑛−2, 𝑘−2) ways:

```py
base = comb(m * n - 2, k - 2) % mod
```

### Calculate Pairwise Manhattan Contributions:

- The Manhattan distance between two pieces can be split into:
  - Horizontal Contribution: Differences along rows.
  - Vertical Contribution: Differences along columns.

Horizontal Contribution:

- For any horizontal distance 𝑑 (from 1 to 𝑛−1):
  - The total distance pairs of cells separated by 𝑑 columns is:𝑑⋅(𝑛−𝑑)
  - There are 𝑛−𝑑 pairs for each pair has distance 𝑑, and this occurs for all 𝑚 rows.
    - each pair has m*m conbinations
  - Total contribution is: 𝑑⋅(𝑛−𝑑)⋅𝑚⋅𝑚

Vertical Contribution:

- For any vertical distance 𝑑 (from 1 to m−1):
  - The total distance of pairs of cells separated by 𝑑 rows is:𝑑⋅(m−𝑑)
  - this occurs for all n columns.
    - each pair has n*n conbinations
  - Total contribution is: 𝑑⋅(m−𝑑)⋅n⋅n
    - If the distance of rows is d = 1, there are m - 1 combination: (0,1),(1,2) ...
    - If the distance of rows is d = 2, there are m - 2 combination: (0,2),(1,3) ...
    - For distance d, there are m - d combinations.
    - For each combination of (xi, xj) above, the xi has n options, xj has n options

The total pairwise Manhattan distance is computed as:

```py
res = 0
for d in range(1, n):
    res += d * (n - d) * m * m
for d in range(1, m):
    res += d * (m - d) * n * n

return res * base % mod
```