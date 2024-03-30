# Intuition

由於`2 <= n == nums.length <= 50` 異常的小
一開始先想brute force, 用C(n, k)找出所有的subseq的暴力搜索可不可行
但會發現這數值會很大

這時就轉向dynamic programming來想

對於subseq.來說, 用dfs搜索的話可以用take-or-skip的方式搜索出k-size的subsequence
並且由於是subseq., 我們事先對nums排序也不影響我們的subseq組合

那這樣我們對nums進行排序後會發現, 這時我們僅需關注我們前一個選擇是什麼, 就能持續求出power
因為power定義是subseq.內任意兩點最短的距離

由於我們nums已經由小到的排過序, 所以這時只需要:

`current_power = min(current_power, nums[i]-nums[prev])`

即可配合top-down dp持續求出power

因此這時我們就能定義

def dfs(i, prev, size, power): the sum of power of subseq. with `size` length and current subseq. power is `power`

那再來就利用take-or-skip找出k-length的subseq.即可, 並且持續更新`power`

```py
@cache
def dfs(i, prev, size, power):
    if size == 0: return power
    if i == n: return 0
    
    power1 = dfs(i+1, prev, size, power) # skip
    power2 = dfs(i+1, i, size-1, min(power, nums[i]-nums[prev] if prev != -1 else inf)) # take
    
    
    return (power1+power2)%mod
    
return dfs(0, -1, k, inf)
```

那麼base case也很理所當然的是:
1. size = 0時, 代表我們找到所需length的subseq.了, 我們返回他的power
2. i==n, 代表我們沒有搜索出合法長度的subseq, 我們就返回0

最終答案就是所有合法的power of subseq.相加並取mod