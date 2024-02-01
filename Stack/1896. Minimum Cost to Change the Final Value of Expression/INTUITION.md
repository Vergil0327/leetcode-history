# Intuition

首先想到leetcode的Basic Calculator
由左往右計算, 遇到括號可利用stack性質

因此如果是單純parse expression的數值的話可以寫出
```py
def parse(expr):
    stack = []
    operator = ""
    cur = 0
    for ch in expr:
        # expression only contains '1','0','&','|','(', and ')'
        if ch.isdigit():
            v = int(ch)
            if operator == "&":
                cur &= v
                operator = ""
            elif operator == "|":
                cur |= v
                operator = ""
            else:
                cur = v
        else:
            if ch == "(":
                stack.append([cur, operator])
                operator = ""
                cur = 0
            elif ch == ")":
                v, op = stack.pop()
                if op == "&":
                    cur = v & cur
                elif op == "|":
                    cur = v | cur
            else:
                operator = ch
```

再來問題就是, 該怎樣以最小次數變換來改變數值
我們能做的有:
- flip "1" into "0"
- flip "0" into "1"
- flip "&" into "|"
- flip "|" into "&"

(XXXX) & (XXXX) = 1&1 = 1 => 變1&0 = 0, cost=min(left_cost, right_cost)
(XXXX) & (XXXX) = 1&0 = 0 => 變0|1 = 1, cost=1
(XXXX) & (XXXX) = 0&1 = 0 => 同上
(XXXX) & (XXXX) = 0&0 = 0 => 變1|0 or 0|1, cost = min(left_cost, right_cost)+1

(XXXX) | (XXXX) = 1|1 = 1 => 變1&0 or 0&1, cost = min(left_cost, right_cost)+1
(XXXX) | (XXXX) = 1|0 = 1 => 變1&0, cost=1
(XXXX) | (XXXX) = 0|1 = 1 => 同上
(XXXX) | (XXXX) = 0|0 = 0 => 變1|0 or 0|1, cost = min(left_cost, right_cost)

所以flip的選擇就這六種, 所以理想上, 我們應該可以在先前value = parse(expression)的過程中
同步把cost給算出來

原本的parse value過程為:
```py
def evalValue(left, right, operator):
    if operator == "&":
        return left&right
    elif operator == "|":
        return left|right
    else:
        return right
    
stack = []
operator = ""
cur = 0

for ch in expression:
    # expression only contains '1','0','&','|','(', and ')'
    if ch.isdigit():
        v = int(ch)
        val = evalValue(cur, v, operator)

    else:
        if ch == "(":
            stack.append([cur, operator])
            operator = ""
            cur = 0
        elif ch == ")":
            v, op = stack.pop()
            val = evalValue(v, cur, op)
            cur = val
        else:
            operator = ch
return cur
```

那現在要同步計算cost的話, 我們原本的`cur`要維護的就不只是value, 還得加上cost
所以`cur = (0, inf)` # value, flip_cost
整體框架變成:

```py    
stack = []
operator = ""
cur = (0, inf) # value, flip_cost

for ch in expression:
    # expression only contains '1','0','&','|','(', and ')'
    if ch.isdigit():
        v = (int(ch), 1)
        val = evalValue(cur, v, operator)
        flip_cost = evalCost(cur, v, operator)
        cur = (val, flip_cost)
    else:
        if ch == "(":
            stack.append([cur, operator])
            operator = ""
            cur = (0, inf)
        elif ch == ")":
            v, op = stack.pop()
            val = evalValue(v, cur, op)
            flip_cost = evalCost(v, cur, op)
            cur = (val, flip_cost)
        else:
            operator = ch
return cur[1]
```

而第一部分:
```py
if ch.isdigit():
    v = (int(ch), 1)
    val = evalValue(cur, v, operator)
    flip_cost = evalCost(cur, v, operator)
    cur = (val, flip_cost)
```

由於我們現在維護的是(value, cost) tuple, 更改`v`這個數的cost只可能是
- 0 flip into 1
- 1 flip into 0
所以`cost=1` => `v = (int(ch), 1)`

再來就如何實現`evalCost`, 回想前面分析的六種cost

1&1 = 1 => 變1&0 = 0, cost=min(left_cost, right_cost)
1&0 = 0 => 變0|1 = 1, cost=1
0&1 = 0 => 同上
0&0 = 0 => 變1|0 or 0|1, cost = min(left_cost, right_cost)+1

1|1 = 1 => 變1&0 or 0&1, cost = min(left_cost, right_cost)+1
1|0 = 1 => 變1&0, cost=1
0|1 = 1 => 同上
0|0 = 0 => 變1|0 or 0|1, cost = min(left_cost, right_cost)

```py
def evalCost(left, right, operator):
    if operator == "&":
        if left[0]+right[0] == 2: # 1&1
            return min(left[1], right[1])
        if left[0]+right[0] == 1: # 1&0 or 0&1
            return 1
        if left[0]+right[0] == 0: # 0&0
            return min(left[1], right[1]) + 1
    elif operator == "|":
        if left[0]+right[0] == 2: # 1|1
            return min(left[1], right[1])+1
        if left[0]+right[0] == 1: # 1|0 or 0|1
            return 1
        if left[0]+right[0] == 0: # 0|0
            return min(left[1], right[1])
    else:
        return right[1]
```

由於現在維護的是一個(value, flip_cost) tuple
所以`evalValue`也得改為
```py
def evalValue(left, right, operator):
    if operator == "&":
        return left[0]&right[0]
    elif operator == "|":
        return left[0]|right[0]
    else:
        return right[0]
```

# Complexity

- time complexity: $O(n)$
- space complexity: $O(stack.size)$