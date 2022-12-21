[55. Jump Game](https://leetcode.com/problems/jump-game/)

`Medium`

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

```
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

Constraints:

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

<details>
<summary>Solution</summary>

这道题表面上不是求最值，但是可以改一改：

请问通过题目中的跳跃规则，最多能跳多远？如果能够越过最后一格，返回 true，否则返回 false。

所以解题关键在于求出能够跳到的最远距离。

[Post](https://labuladong.github.io/algo/3/29/102/)

```java
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int farthest = 0;
        for (int i = 0; i < n - 1; i++) {
            // 不断计算能跳到的最远距离
            farthest = Math.max(farthest, i + nums[i]);
            // 可能碰到了 0，卡住跳不动了
            if (farthest <= i) {
                return false;
            }
        }
        return farthest >= n - 1;
    }
}
```
</details>