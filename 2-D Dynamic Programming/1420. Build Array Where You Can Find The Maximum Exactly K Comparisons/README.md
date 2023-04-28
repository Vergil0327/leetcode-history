[1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)

`Hard`

You are given three integers `n`, `m` and `k`. Consider the following algorithm to find the maximum element of an array of positive integers:

```
maximum_value = -1
maximum_index = -1
search_cost = 0
n = arr.length
for (i = 0; i < n; i++) {
    if (maximum_value < arr[i]) {
        maximum_value = arr[i]
        maximum_index = i
        search_cost = search_cost + 1
    }
}
return maximum_index
```

You should build the array arr which has the following properties:

- `arr` has exactly `n` integers.
- `1 <= arr[i] <= m` where (0 <= i < n).
- After applying the mentioned algorithm to arr, the value `search_cost` is equal to `k`.

Return the number of ways to build the array `arr` under the mentioned conditions. As the answer may grow large, the answer must be computed modulo $10^9$ + 7.

```
Example 1:
Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

Example 2:
Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.

Example 3:
Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

Example 4:
Input: n = 50, m = 100, k = 25
Output: 34549172
``` 

Constraints:

- 1 <= n <= 50
- 1 <= m <= 100
- 0 <= k <= n

Acceptance Rate
63.0%

<details>
<summary>Hint 1</summary>

Use dynamic programming approach. Build dp table where dp[a][b][c] is the number of ways you can start building the array starting from index a where the search_cost = c and the maximum used integer was b.

</details>

<details>
<summary>Hint 2</summary>

Recursively, solve the small sub-problems first. Optimize your answer by stopping the search if you exceeded k changes.

</details>

<details>
<summary>Video Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=9epbhqVpzyI&t=3s&ab_channel=HuifengGuan)
</details>
