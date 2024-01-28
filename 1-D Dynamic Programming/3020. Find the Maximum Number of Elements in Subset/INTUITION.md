# Intuition

```
2
2 2 4
2 2 4 4 16

1 2 3 4 
{1 1} 1 {1 1} | 1
{1 1 1} 1 {1 1 1}
```

先列出一些examples
我們要找出最長的[2個x, 2個x^2, 兩個x^4, ...] + 1個x^k

扣掉中間的x^k, 前面那段這讓我想到longest increasing subsequence (LIS)
只是這次我們能接在LIS後面的條件是只有當`count[nums[i]] >= 2 and count[sqrt(nums[i])] >= 2`

所以這邊先想到個框架是:

1. 我們先求出`Counter(nums)`
2. 然後我們定義dp: the longest length of [2,2,2,2...] pattern ended at nums[i]
   - ex. dp[4] = [2,2,4,4]
   - ex. dp[2] = [2,2]
3. 然後我們**排序**, 由小到大遍歷**distinct nums[i]**來更新`dp[num]`
   - 首先如果count[num] >= 2, dp[num] = 2
   - 再來就LIS的概念, 令`x = int(sqrt(num))`, 如果count[x] >= 2 and count[num] >= 2, 那麼我們可以append兩個num接在x後面, `dp[num] = dp[x] + 2`
   - 同時在遍歷過程中更新我們的最長pattern length, 以num結尾, 看以`x`結尾的最長LIS有多長, `res = max(res, dp[x] + 1)`
4. 過程中必須保證`x^2 == nums[i]`, 所以我們確認一下`x == int(sqrt(nums[i])) and x^2 must equal num`
 
```py
count = Counter(nums)
for num in sorted(count.keys()):
    if count[num] >= 2:
        dp[num] = 2

    x = int(sqrt(num))
    if pow(x, 2) == num and x != num:
        if count[num] >=2 and count[x] >= 2:
            dp[num] = max(dp[num], dp[x]+2)
        res = max(res, dp[x]+1)
```

但仔細看一下`nums[i]==1`這個case:
```
nums = [1,1,1,1] => expected = 3
nums = [1,1,1] => expected = 3
```

1的開平方還是1, 所以1這個edge case我們單獨處理
以1結尾的valid pattern為: `endAt1 = 1 + ((count[1]-1)//2) * 2`

所以最終答案就兩個可能case取最大: max(res, endAt1)

time: O(nlogn)