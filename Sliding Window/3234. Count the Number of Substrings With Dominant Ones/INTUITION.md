# Intuition

[推薦詳細解說 by HuifengGuan](https://www.youtube.com/watch?v=vKGsBR8N_HU&ab_channel=HuifengGuan)

首先簡單分析一下:
11111 = (1, 1, 1, 1, 1) + (11, 11, 11, 11) + (111, 111) + (1111, 1111) + (11111) = (1 + # of 1) * # of 1 / 2
然後每個1...1都可以往前往後搜有多少相鄰zeros, zeros最多可以有int(sqrt(# of 1))個

根據constraint: 1 <= s.length <= 4 * 10^4 => 代表0的個數介於 [1, sqrt(4*10^4) = 200]之間
這數值不大, 所以如果我們遍歷所有可能的0, 然後在以O(n)時間找出相對應合法的1所組成的substr
整個時間複雜度會是O(200n) ~ O(10^6) => 這是可以接受的時間複雜度

因此我們的目標就是遍歷所有可能的`0`數目, 然後去看恰好含有這麼多個`0`的substr有多少個是合法
=> 這邊我們能用two pointers (sliding window)去找出符合`0`個數substr

那再來就是要想我們要如何根據現在的`0`去找出合法substr, 也就是我們要對當前這段substr去往外拓展使得`1`的數目符合題意的
`the number of ones in the string is greater than or equal to the square of the number of zeros in the substr`


```
X X X X X X X X {1 1 1 1 1 ...}
l             r
   含有k個0 => 合法substr必須至少有k*k個1
   所以如果s[l:r]這段已經含有x個1了, 我們在`r`這位置往後只需要再找k*k-x個1即可找到1個合法substr
   那如果右邊總共有m個1, 並且x + m >= k*k的話, 那代表結合這m個1, 總共有x+m - k*k個合法substr
```

根據以上分析, 我們還會需要每個index位置的右邊有多少連續的1, 而這個可以預先處理存在right_ones[idx]裡

整體框架會像這樣:

其中right_one[idx]為: 從idx位置開始, 有多少連續個1

```py
n = len(s)

right_one = [0] * (n+1)
for i in range(n-1, -1, -1):
    if s[i] == "1":
        right_one[i] = right_one[i+1]+(s[i]=="1")

ones = sum(1 for ch in s if ch == "1")
res = 0
for require_zero in range(1, ceil(sqrt(ones))+1):
    l = r = zero = 0
    while r < n:
        zero += int(s[r] == "0")
        r += 1
        while l < r and zero >= require_zero:
            one = r-l-zero
            if right_one[r] + one >= zero*zero:
                need_ones = max(0, zero*zero-one) # zero*zero-one 可能出現負數
                res += max(0, right_one[r] - need_ones + 1) # 可能出現負數
            zero -= int(s[l] == "0")
            l += 1

return res
```

但在考慮`0`個數落在[1, 200]的全部可能後, 還得考慮不包含`0`的連續1的貢獻

也就是如果s = "0011"
right_one = [0,0,2,1,0]

- 對於idx=0,1, 都是"0"開頭, 不是我們要考慮的連續"1...1"
  - 含有"0"的合法substr數目已在sliding window的部分計算過了
- 對於idx=2來說, "11", "1"都是合法substr
- 對於idx=3來說, "1"是合法substr

所以對於那些連續1的貢獻, 我們可以這麼計算

```py
for i in range(n):
    res += right_one[i]
```