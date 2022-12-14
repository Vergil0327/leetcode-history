[1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/)

`Medium`

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

```
Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
```

Constraints:

- 1 <= s.length <= 10^5
- s consists of '(' and ')' only.

<details>
<summary>Hint 1</summary>

Use a stack to keep opening brackets. If you face single closing ')' add 1 to the answer and consider it as '))'.

</details>

<details>
<summary>Hint 2</summary>

If you have '))' with empty stack, add 1 to the answer, If after finishing you have x opening remaining in the stack, add 2x to the answer.

</details>

<details>
<summary>Hint 3</summary>

Follow-Up of 921. Minimum Add to Make Parentheses Valid
</details>

<details>
<summary>Solution 1</summary>

[Lee215](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/solutions/780199/java-c-python-straight-forward-one-pass/?orderBy=most_votes)

```python
    def minInsertions(self, s):
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
```
</details>

<details>
<summary>Solution 2</summary>

[detailed explanation](https://labuladong.github.io/article/fname.html?fname=%E6%8B%AC%E5%8F%B7%E6%8F%92%E5%85%A5)

遍歷字符串，通過一個 `need` 變量記錄對右括號的需求數，根據 `need` 的變化來判斷是否需要插入。

類似 921. 使括號有效的最少添加，當 `need` == -1 時，意味著我們遇到一個多餘的右括號，顯然需要插入一個左括號。

另外，當遇到左括號時，若對右括號的需求量為奇數，需要插入 1 個右括號，因為一個左括號需要兩個右括號嘛，右括號的需求必須是偶數，這一點也是本題的難點。

首先，當 need == -1 時，意味著我們遇到一個多餘的右括號，顯然需要插入一個左括號。

比如說當 s = ")"，我們肯定需要插入一個左括號讓 s = "()"，但是由於一個左括號需要兩個右括號，所以對右括號的需求量變為 1：


```java
if (s.charAt(i) == ')') {
    need--;
    if (need == -1) {
        res++;
        need = 1;
    }
}
```

另外，當遇到左括號時，若對右括號的需求量為奇數，需要插入 1 個右括號。因為一個左括號需要兩個右括號嘛，右括號的需求必須是偶數，這一點也是本題的難點。

所以遇到左括號時要做如下判斷：

```java
if (s[i] == '(') {
    need += 2;
    if (need % 2 == 1) {
        // 插入一个右括號
        res++;
        // 對右括號的需求减一
        need--;
    }
}
```

總和變成
```java
class Solution {
    public int minInsertions(String s) {
        int res = 0, need = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                need += 2;
                if (need % 2 == 1) {
                    res++;
                    need--;
                }
            }

            if (s.charAt(i) == ')') {
                need--;
                if (need == -1) {
                    res++;
                    need = 1;
                }
            }
        }

        return res + need;
    }
}
```
</details>
