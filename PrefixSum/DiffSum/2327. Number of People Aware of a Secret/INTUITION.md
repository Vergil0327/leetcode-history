# Intuition

首先先模擬整個過程

day 1:

在day1的人可以告訴`[day1+delay,day1+forget)`這範圍的人(left inclusive, right exclusive)

但在day1+forget的時候, day1的人會忘記秘密

day 2:
在day2的人可以告訴`[day2+delay,day2+forget)`這範圍的人(left inclusive, right exclusive)

但在day2+forget的時候, day2的人會忘記

所以我們用一個dp array來定義:

dp[day] = # of person who knows the secrets

所以整個狀態轉移為:
遍歷day from 1 to n
1. 當在dp[day]時, 可以更新dp[day+delay,day+forget-1]
2. 但day-forget >= 0時, dp[day-forget] = 0

```py
for day in range(1, n+1):
    start, end = day+delay, min(n+1, day+forget)
    for i in range(start, end):
        dp[i] += dp[day]

    if day-forget >= 0:
        dp[day-forget] = 0 # forget
```

**base case**
在day1的時候有一個人知道秘密
dp[1] = 1

那最後答案就看還有多少人知道秘密 => `sum(dp)`


# Optimization

延續上面思想dp[i]一樣紀錄在i-th day有多少人知道秘密
但其實內層循環每次都更新一段[start,end)的區間
所以我們可以用diff array來標記這段區間, 紀錄在i-th day還有多少人可以告訴秘密給別人
藉此簡化內層循環

```py

dp = [0] * (n+1)
diff = [0] * (n+1)

# base case
diff[1] += 1
diff[2] -= 1

for i in range(1, n+1):
    dp[i] = dp[i-1] + diff[i]

    if i+delay <= n:
        diff[i+delay] += dp[i]
    if i+forget <= n:
        diff[i+forget] -= dp[i]

    if i-forget >= 0:
        dp[i-forget] = 0 # forget

return sum(dp)%mod
```