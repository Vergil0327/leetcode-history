[343. Integer Break](https://leetcode.com/problems/integer-break/description/)

`Medium`

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

```
Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

Constraints:

- 2 <= n <= 58

<details>
<summary>Hint 1</summary>

There is a simple O(n) solution to this problem.

</details>

<details>
<summary>Hint 2</summary>

You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

</details>

<details>
<summary>Solution 1</summary>

[HuifengGuan](https://www.youtube.com/watch?v=BhxOcwiOTCM)
</details>

<details>
<summary>Solution 2</summary>

  integerBreak(4)
= max(1 * 3, 1 * integerBreak(3), 2 * 2, 2 * integerBreak(2), integerBreak(2) * 2, integerBreak(2) * integerBreak(2)
= max(
    max(1, integerBreak(1)) * max(3, integerBreak(3)),
    max(2, integerBreak(2)) * max(2, integerBreak(2))
)

int res = Integer.MIN_VALUE;
for (int i = 1; i <= n; i++) {
    res = max(res,
            max(integerBreak(i), i) * max(integerBreak(n - i), n - i)
    );
}

加上Memorization後就消除重疊子問題，將時間複雜度降至 O(N)

```java
class Solution {
    int[] memo;

    public int integerBreak(int n) {
        memo = new int[n + 1];
        return dp(n);
    }

    // 定义：拆分 n 获得的最大乘积为 dp(n)
    int dp(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (memo[n] > 0) {
            return memo[n];
        }

        // 状态转移方程
        int res = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            res = Math.max(res,
                    Math.max(dp(i), i) * Math.max(dp(n - i), n - i)
            );
        }
        memo[n] = res;
        return res;
    }
}
```
</details>

<details>
<summary>Solution 3</summary>

[Math Solution](https://leetcode.com/problems/integer-break/solutions/80689/a-simple-explanation-of-the-math-part-and-a-o-n-solution/)
</details>