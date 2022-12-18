[514. Freedom Trail](https://leetcode.com/problems/freedom-trail/description/)

`Hard`

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
 
```
Example 1:
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Example 2:
Input: ring = "godding", key = "godding"
Output: 13
```

Constraints:

- 1 <= ring.length, key.length <= 100
- ring and key consist of only lower case English letters.
- It is guaranteed that key could always be spelled by rotating ring.

<details>
<summary>Solution 1</summary>

[labuladong](https://labuladong.github.io/algo/3/28/88/)

基本思路
dp 函数的定义如下：当圆盘指针指向 ring[i] 时，输入字符串 key[j..] 至少需要 dp(ring, i, key, j) 次操作。

根据这个定义，题目其实就是想计算 dp(ring, 0, key, 0) 的值，base case 就是 dp(ring, i, key, len(key)) = 0。

```java
class Solution {
    public:
    // 字符 -> 索引列表
    unordered_map<char, vector<int>> charToIndex;
    // 备忘录
    vector<vector<int>> memo;

    /* 主函数 */
    int findRotateSteps(string ring, string key) {
        int m = ring.size();
        int n = key.size();
        // 备忘录全部初始化为 0
        memo.resize(m, vector<int>(n, 0));
        // 记录圆环上字符到索引的映射
        for (int i = 0; i < ring.size(); i++) {
            charToIndex[ring[i]].push_back(i);
        }
        // 圆盘指针最初指向 12 点钟方向，
        // 从第一个字符开始输入 key
        return dp(ring, 0, key, 0);
    }

    // 计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
    int dp(string& ring, int i, string& key, int j) {
        // base case 完成输入
        if (j == key.size()) return 0;
        // 查找备忘录，避免重叠子问题
        if (memo[i][j] != 0) return memo[i][j];

        int n = ring.size();
        // 做选择
        int res = INT_MAX;
        // ring 上可能有多个字符 key[j]
        for (int k : charToIndex[key[j]]) {
            // 拨动指针的次数
            int delta = abs(k - i);
            // 选择顺时针还是逆时针
            delta = min(delta, n - delta);
            // 将指针拨到 ring[k]，继续输入 key[j+1..]
            int subProblem = dp(ring, k, key, j + 1);
            // 选择「整体」操作次数最少的
            // 加一是因为按动按钮也是一次操作
            res = min(res, 1 + delta + subProblem);
        }
        // 将结果存入备忘录
        memo[i][j] = res;
        return res;
    }
};
```
</details>

<details>
<summary>Solution 2</summary>

[HuifengGuan](https://www.youtube.com/watch?v=1ErNzKfRrX8)
</details>