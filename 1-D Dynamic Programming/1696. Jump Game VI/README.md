[1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

`Medium`

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

```
Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
```

Constraints:

- 1 <= nums.length, k <= 10^5
- -10^4 <= nums[i] <= 10^4

<details>
<summary>Hint 1</summary>

Let dp[i] be "the maximum score to reach the end starting at index i". The answer for dp[i] is nums[i] + max{dp[i+j]} for 1 <= j <= k. That gives an O(n*k) solution.

</details>

<details>
<summary>Hint 2</summary>

Instead of checking every j for every i, keep track of the largest dp[i] values in a heap and calculate dp[i] from right to left. When the largest value in the heap is out of bounds of the current index, remove it and keep checking.

</details>

<details>
<summary>Solution</summary>

[HuifengGuan](https://www.youtube.com/watch?v=f4fEdD0IbEc)

Sliding Window Maximum

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = nums[0]
        q = collections.deque([(0, nums[0])])

        for i in range(1, n):
            # Pop out of range elements
            if q and q[0][0] < i-k:
                q.popleft()

            # Update dp result with q
            dp = q[0][1] + nums[i]

            # Make q monotonically decreasing
            while q and dp > q[-1][1]:
                q.pop()

            # Add i to the correct place in q
            q.append((i, dp))

        return dp
```
</details>