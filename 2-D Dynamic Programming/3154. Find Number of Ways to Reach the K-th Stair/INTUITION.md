# Intuition

```
x op1: -x
y op2:
    - 1: 1+2^0 = 2 = 2^1
    - 2: 1+2^0+2^1 = 4 = 2^2
    - 3: 1+2^0+2^1+2^2 = 8 = 2^3
```

we want to use **x op1 + y op2 to reach k**

比較直覺的想法就是用dfs去模擬搜索
def dfs(i, x, y, op): the total number of ways to reach stair k where:
- x means back steps from op1
- y means jump of op2 in description
- op = 1 or 2 which means op1 or op2

如此一來可以寫出:

```py
op1, op2 = 1, 2

@cache
def dfs(i, op, jump, back):
    if i > k+1: return 0 # no way to turn back

    res = 1 if i == k else 0 # keep exploring possible ways even when we already reach k position

    if op == op2: # op1 can't consecutive
        res += dfs(i-1, op1, jump, back+1)
    res += dfs(i+power2[jump], op2, jump+1, back)
```

但仔細看了一下會發現我們不需要把back step也考慮進state裡 (完全沒用到)
所以最後:

```py
@cache
def dfs(i, op, jump):
    if i > k+1: return 0 # no way to turn back

    res = 1 if i == k else 0 # keep exploring possible ways even when we already reach k position

    if op == op2: # op1 can't consecutive
        res += dfs(i-1, op1, jump)
    res += dfs(i+power2[jump], op2, jump+1)

    return res
```

比較重要的關鍵條件是:
1. base case: if i > k+1: return 0 # 無法再回頭
2. see example2, 即使已經抵達k, 也可能過頭後再回頭一次抵達k, res = 1 if i == k else 0

# Intuition 2

Solve integer pair (x,y) in the equation
k=2^x−y where x=number of operations of 2nd type, y=number of operations of 1st type, due to the restriction it holds that y≤x+1 (op1 can't be consecutive)
=> y = 2^x - k => 我們要解出這式子的可能答案

所以我們我們如果op2 jump了**x**次, 由於op1不可連續, 所以我們僅最多有x+1次op1往下
然後必須往下 `pow(2, x) - k` 這麼多

令a = x+1, b = pow(2, x) - k
方法數總共有 combination(a, b)

由於 k <= 10^9, jump的上限為`upperbuond = ceil(log2(pow(10, 9)))`
Iterate x from 0 to **upperbuond**, and accumulate the combinations.