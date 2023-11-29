[2407. Longest Increasing Subsequence II](https://leetcode.com/problems/longest-increasing-subsequence-ii/)

`Hard`

You are given an integer array nums and an integer k.

Find the longest subsequence of nums that meets the following requirements:

The subsequence is strictly increasing and
The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

```
Example 1:
Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation:
The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.

Example 2:
Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation:
The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.

Example 3:
Input: nums = [1,5], k = 1
Output: 1
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.
```

Constraints:

- 1 <= nums.length <= 105
- 1 <= nums[i], k <= 105

<details>
<summary>Hint 1</summary>

We can use dynamic programming. Let dp[i][val] be the answer using only the first i + 1 elements, and the last element in the subsequence is equal to val.
</details>

<details>
<summary>Hint 2</summary>

The only value that might change between dp[i - 1] and dp[i] are dp[i - 1][val] and dp[i][val].
</details>

<details>
<summary>Hint 3</summary>

Try using dp[i - 1] and the fact that the second last element in the subsequence has to fall within a range to calculate dp[i][val].
</details>

<details>
<summary>Hint 4</summary>

We can use a *segment tree* to find the maximum value in dp[i - 1] within a certain range.
</details>

<details>
<summary>solution</summary>

```python
class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

class Solution:
    def lengthOfLIS(self, A: List[int], k: int) -> int:
        n, ans = max(A), 1
        seg = SEG(n)
        for a in A:
            a -= 1
            premax = seg.query(max(0, a - k), a)
            ans = max(ans, premax + 1)
            seg.update(a, premax + 1)
        return ans
```
</details>