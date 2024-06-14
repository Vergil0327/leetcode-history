# Intuition

可以先對rewards預處理, 因為必須**greater than marked element**, 我們不會選擇同個nums[i]兩次

```py
arr = list(sorted(set(rewards))) # we won't select same rewards[i] twice
```

再來我們就brute force + memorization => dynamic programming

定義dp[x]: the maximum total reward we can collect if our picked subseq. ended at x

```
rewards = [X X X X X X X X X X] X
                                i
```

我們考慮地i-th reward, 如果我們要挑他, reward[i]
根據題意, **If rewardValues[i] is greater than your current total reward x, then add rewardValues[i] to x**, 
reward[i]可以接在[0, reward[i])後面, 所以我們全部遍歷一遍去更新dp

```py
arr = list(sorted(set(rewards))) # we won't select same rewards[i] twice
dp = [0]*(arr[-1]*2+1)
n = len(arr)

for i in range(n):
    for x in range(arr[i]):
        dp[arr[i] + dp[x]] = arr[i] + dp[x]
return max(dp)
```

但可惜這樣會TLE, 這題也沒有太好的算法
Hint4給的只是透過bit manipulation去做點小優化(constant optimization) => 透過[Bitsets](https://www.youtube.com/watch?v=jqJ5s077OKo&ab_channel=ErrichtoAlgorithms)的概念

對於arr[i]來說, 我們原本要遍歷[0, arr[i])去更新dp
我們將這步改為: **mask = (1<<arr[i])-1**
[0, arr[i])這範圍我們改成用bitmask來表示, bitmask上的每一位即代表[0, arr[i]) (right-exclusive)
第1個bit=0, 第2個bit=1, ..., 直到第i+1個bit=arr[i]
然後用bit = 0/1來表示該bit所代表的數值存不存在於dp裡


那這樣原本[0, arr[i])這範圍內, 我們可以透過這步`(x&mask)`, 即可知道之前的所有dp values

或者我們舉例來說:

然後一開始=0 => 我們也改成用bitmask表示, dp_mask=0b1
=> bitmask第一位bit代表x=0, 存在於dp 裡
假設arr[i] = 3, 那麼mask = (1<<arr[i])-1 = 0b11 => 代表[0, arr[i])這範圍
mask & dp_mask = 1 => 得到先前的所有可能dp values, 1代表x=0
考慮挑選arr[i]的情況 => 原本是dp[arr[i] + dp[x]] = arr[i] + dp[x]
現在改用bitmask紀錄, 所以是將(mask & dp_mask)<<arr[i]加入到dp_mask裡
這時dp_mask = 1001, 他代表的就是我們原本的dp array
我們可以直接透過dp_mask看出:

```
dp_mask = ...001001
          ...543210

代表3跟0這兩個位置的bit是1, 代表這兩個dp value是存在的
```

最後由於我們是要找max(dp), 相當於我們要找最左邊的bit的值是多少
由於第一位bit代表x=0, 所以最左邊的bit的值就代表整個dp_mask的長度-1
所以我們直接返回dp_mask.bit_length() - 1即可 (0-indexed)