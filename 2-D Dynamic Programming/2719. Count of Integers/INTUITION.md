# Intuition

我們要遵守兩個條件:
1. x必須介於`num1`跟`num2`之間
2. digit_sum(x)必須介於`[min_sum, max_sum]`

其中num1, num2 介於[1, 10^22]之間，相當大
因此遍歷這範圍找出合法解肯定是不行的

然後我們看到min_sum跟max_sum最大不超過400, 因此我們應該要從這邊下手

那既然著眼於digit sum, 那麼我們就digit by digit來看
並且我們要求有多少個並且對10^9+7取餘, 那這肯定是DP

那麼我們可以有個很容易想到的想法是:
- 如果我們知道`<= num2`的合法解有`x`
- 而`< num1`的合法解有`y`
那麼答案是不是就是 `x-y`?

所以我們大致上會有個這麼一個關係式:
`answer = f(max_sum) - f(min_sum-1)`

再來由於是dp, 我們一個位數一個位數來看:

```
X X X X X X X X X
                i
```
對於第i個位置來說, 我們有`0-9`十個選擇
但我們是不是每個都可以選?

我們先看這個例子: `num2 = "18"`
如果要構造出的digits, `s`, 不超過`num2`的情況的話

我們`i=0`, 有兩種選擇
1. append "0"
   - 如果我們第一位數是0, 那麼我們在`i=1`的位數, `0-9`都是合法不超過num2的
2. append "1"
    - 如果我們第一位數是1, 那麼在`i=2`的位數, 只能選`0-8`, 不然就會超過num2

所以很明顯的, 根據前一個選擇會影響當下的合法狀態
那這題最重要的突破口就是如何決定出這個範圍?

如果我們紀錄我們直至當前所構造出的string `s`的話, 經由跟`num2`比對:

- 如果前`i-1`位數, s[:i-1] == num2[:i-1]的話, 那麼s[i]最高就只能取`[0,num2[i]]`這區間
- 但如果前`i-1`位數中, s[:i-1]已經比num2[:i-1]小的話, 那麼s[i]就[0,9]都是可以合法選取的

所以關鍵就是前面`i-1`位數是不是已經取到邊界值了
- 如果是, 那麼s[i]最多只能取到num2[i]
- 如果不是, 那麼s[i]可以自由從[0,9]中選取

所以我們可以用個變數isUpperbound來記錄這個訊息:
`hi = int(num2[i]) if isUpperbound else 9`

同理, 我們構造的string也必須`>= num1`
所以一樣用一個變數`isLowerbound`來紀錄:
`lo = int(num1[i] if isLowerbound else 0)`

所以我們如果是top-down的方式來構造這個string的話:
我們就持續看到目前為止構造的string `s`, 是不是已經貼到`upperbound`或`lowerbound`邊界並構造答案

那這樣我們就能求出介於num1及num2之間的所有string

```py
def calculate(i, isLowerbound, isUpperbound):
    if i == len(num2): return 1

    lo = int(num1[i]) if isLowerbound else 0
    hi = int(num2[i]) if isUpperbound else 9

    res = 0
    for c in range(lo, hi+1):
        res += calculate(
            i+1,
            True if isLowerbound and c == lo else False,
            True if isUpperbound and c == hi else False
        )
    return res
```

**那這邊記得將num1補到相同位數**

ex. num1 = "8", num2 = "1234"
我們可以想成num1="0008", num2 = "1234
那這樣就是digit by digit的構造出
"0008" ~ "1234"的所有數值

由於我們還必須確保我們當前的digit_sum(s)必須介於[min_sum, max_sum]之間

由於我們一開始的high level的思想是: `answer = f(max_sum) - f(min_sum-1)`

所以相當於:

`answer = calculate(i, isLowerbound, isUpperbound, max_sum) - calculate(i, isLowerbound, isUpperbound, min_sum-1)`

所以我們在構造的過程中必須還要紀錄我們當前digit_sum的狀態, 只有digit_sum <= constraint才是合法的

```py
def calculate(i, isLowerbound, isUpperbound, digit_sum):
    if digit_sum < 0: return 0 # 由於digit_sum不合法, 所以當前s不是合法解
    if i == len(num2): return 1 # 當前構造的s是合法的, 計數+1

    lo = int(num1[i]) if isLowerbound else 0
    hi = int(num2[i]) if isUpperbound else 9

    res = 0
    for c in range(lo, hi+1):
        res += calculate(
            i+1,
            True if isLowerbound and c == lo else False,
            True if isUpperbound and c == hi else False,
            digit_sum - c
        )
        res %= mod
    return res
```

那最終答案就是:

```py
total = calculate(0, 1, 1, max_sum)
invalid = calculate(0, 1, 1, min_sum-1)

# 由於我們有對數值取餘, 所以兩者相減可能會是負數
# 這時必須`(num+mod)%mod`
return ((total-invalid)%mod + mod )%mod
```

# Complexity

- time complexity

$$O(num2.length * 2 * 2 * max_sum * 10)$$
- space complexity
$$O(num2.length * 2 * 2 * max_sum)$$