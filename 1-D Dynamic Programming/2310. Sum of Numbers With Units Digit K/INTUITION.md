# Intuition

```
    k => keep searching num-k
   Xk => keep searching num-Xk
  XXk ...
 XXXk
XXXXk

base case: num == 0
```

其實有點像是我們有一堆尾數為`k`的coin, 然後希望無限次用這些coin來讓num變為0
所以我們家先找出這些coin, 然後在用top-down dp搜索即可

首先找出合法coins, 條件是長度不超過num (不可能用10000在num=1000上)
並且coin必須**大於0**

```py
# find all valid integers first
digits = set([str(k)])
length = 1
while length <= len(str(num)):
    nxt = digits.copy()
    for digit in digits:
        for d in range(10):
            nxt.add(str(d) + digit)
    digits = nxt
    length += 1
digits = set([int(digit) for digit in digits if int(digit) > 0])
```

再來就用試著分配這些coin即可

```py
@cache
def dfs(num):
    if num < 0: return inf
    if num == 0: return 0

    res = inf
    for digit in digits:
        if num >= digit:
            print(num, digit)
            res = min(res, dfs(num - digit) + 1)
    return res

ans = dfs(num)
return ans if ans < inf else -1
```

# Math solution

[original post](https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/solutions/2168211/c-short-and-easy-with-math/)


依據題意, 對於這個possible set:

$A1 + A2 + ... + An = n*k + 10*(a1 + a2 + .. + an) = sum$

由於`10*(a1 + a2 + .. + an)%10`這項永遠是0

所以我們要找就是一個符合`(n*k)%10 + 0 == sum%10`的possible set

```py
def minimumNumbers(self, num, k):
    if num == 0: return 0
    for n in range(1, 11):
        if k * n % 10 == num % 10 and n * k <= num:
            return n
    return -1
```

至於為什麼set size `n <= 10`, 這是因為超過之後, 尾數的digit就開始重複了, 而我們僅關注尾數digit


k = 9:

- 9 * **1** = **9**
- 9 * 1**1** = 9**9**
- 9 * **2** = 1**8**
- 9 * 1**2** = 10**8**
- 9 * **3** = 2**7**
- 9 * 1**3** = 11**7**
