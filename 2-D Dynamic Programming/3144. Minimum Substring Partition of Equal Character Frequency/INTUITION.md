# Intuition

看題意求極值**the minimum number of substrings that you can partition s into.**首先想到的是利用DP

先試著照題意定義: dp[i]: the minimum number of balanced substring considering first i elements

X X X X {X X X X X}
       <-j       i
那再來看狀態轉移: if s[j:i] balanced => dp[i] = min(dp[i], dp[j-1]+1)

所以整體框架可以很快地寫出, 這邊我們用1-indexed來避免dp[j-1] out-of-bounds:

```py
n = len(s)
s = "#" + s
dp = [inf]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(i, 0, -1):
        if balanced:
            dp[i] = min(dp[i], dp[j-1]+1)
return dp[n]
```

那剩下要解決的就是如何以O(1)時間判斷當前substring是否balanced
balanced的定義是:每個字母的個數相同
所以首先我們先用一個hashmap來記錄字母的個數
然後再額外利用一個hashmap來記錄當前字母個數有幾種

ex. 我們用`count[ch]`來記錄`ch`這字母的個數
然後再利用`occur[count[ch]]`來記錄當前有幾個字母是`count[ch]`長度
```py
count[ch] += 1
occur[count[ch]] += 1
```

但別忘記得再更新`count[ch] += 1`前, 先更新occur[count[ch]], 所以邏輯上順序會是:

```py
if count[ch] > 0:
    occur[count[ch]] -= 1
    if occur[count[ch]] == 0:
        del occur[count[ch]]
count[ch] += 1
occur[count[ch]] += 1
```

那這樣我們就能利用**len(occur) == 1**來判斷當前s[j:i]是不是balanced
如果**len(occur) == 1**成立, 那麼dp[i] = min(dp[i], dp[j-1] + 1)

時間複雜度: O(n^2)