# Intuition
only 2 possible intitial value for `original` array: `0` or `1`

- construct `original[i+1]` based on `derived[i]`
- check if `original[n-1] XOR original[0]` equals derived[n-1]

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Other Solution - 1

但實際上, 如果我們一開始的state為`0`

- 如果derived[i] == 0: 代表下個state跟當前state相同
- 如果derived[i] == 1: 代表下個state跟當前state不同

全部更新完後我們再看最後的stateu有沒有等同於一開始的state, i.e. `0`

```py
state = 0

n = len(derived)
for i in range(n):
    if derived[i]:
        state = 1-state
return state == 0
```

# Other Solution - 2

有個更精妙的解法是

derived[i] = original[i] ^ original[i+1]
XOR(derived[i] for i in range(n)) = (original[i] ^ original[i+1]) ^ (original[i+1] ^ original[i+2]) ^ ...
                                  = 0

所以我們僅需要判斷有沒有滿足`XOR(derived[i]) = 0`這個條件
所以:

```py
n = len(derived)

state = 0
for i in range(n):
    state ^= derived[i]
return state == 0
```

1^1 = 0
1^1^1 = 1
或者也可以想成裡面`1`的個數必須是偶數
```py
return sum(derived)%2 = 0
```