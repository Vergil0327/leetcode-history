# Intuition

我們不用管string組成怎樣，我們只要關注目前有幾個`Absent`以及`Trailing Late`即可

如果是top-down:
1. 每當加上`Absent`或`Present`，`Trailing Late`都會歸零
2. `Absent`個數最多1個
3. `Trailing Late`最多兩個

再加上memorization，即可達到:
time complexity: O(n)
space complexity: O(n * 2 * 3)

同樣地，我們也能改成bottom-up形式

定義 `dp[i][absent][trailingL]: the number of possible attendance records of length i with absent and trailingL`
