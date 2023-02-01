# Intuition

因為只要是非空的sequence都是答案，因此我們用DFS進行backtracking，找出每個可以加上字符的點去組成排列，並利用hashset去除重複

最終hashset的大小極為答案

# Complexity

- time complexity

$$O(2^n * (n * n))$$
`# of subproblems * complexity of subproblem`
iterate state -> O(n)
string formation (state[:j] + tiles[i] + state[j:]) -> O(n)