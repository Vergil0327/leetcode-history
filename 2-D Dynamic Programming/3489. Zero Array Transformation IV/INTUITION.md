# Intuition

[Great Explanation Here by @HuifengGuan](https://www.youtube.com/watch?v=ilvbOwh1o_U&ab_channel=HuifengGuan)

一開始想到difference array跟binary search去猜要用到多少個queries
但發現都不適用, 因為這題是要每個nums[i]都是要**剛好**扣掉數個queries[i][2]後變為0
也就是k個queries內, 對於每個nums[i]來說, 這k個queries每個丟可選可不選, 最後扣掉後要剛好為0

在看了一下限制發現, 從nums[i]跟queries.length的範圍, 是允許O(n^2)的, 並且nums.length也很小, 算上去也可接受

- 1 <= nums.length <= 10
- 0 <= nums[i] <= 1000
- 1 <= queries.length <= 1000

因此想到這題可能是要用到dynamic programming, 但沒寫出來就是

看了才發現, 能否將nums[i]透過一個subset的queries[j]來變為零, 這其實就是個0/1背包問題

所以如果我們定義: `dp[i][num]: whether the i-th element which equals num can be reduce to zero`

那麼我們就能在遍歷queries[k]的過程中持續更新這個dp, 然後再檢查每一輪更新後
是否能將整個`nums`剛好都化為0

那整體框架如下:

m個背包每個可用可不用
每個背包能對[l,r]區間的nums[i]進行更新, 遍歷所有nums[i]的可能值域(0<=nums[i]<=1000)

> 這邊注意, 由後往前遍歷是為了避免dp[i][nums[i]]依賴到dp[i][nums[i']] where nums[i] > nums[i-val] and dp[i][i-val] has been already updated

```py
for k in range(m):
    l, r, val = queries[k]
    for i in range(l, r+1):
        for num in range(1000, -1, -1):
            if num-val >= 0 and dp[i][num-val]:
                dp[i][num] = True
    if all(dp[j][nums[j]] for j in range(n)): return k+1
return -1
```