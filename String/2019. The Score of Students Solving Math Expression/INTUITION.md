# Intuition

如果只是要計算正確值的話, 直接用227. Basic Calculator II即可

```py
def basicCalculatorII(s: str) -> int:
    n = len(s)

    op = "+"
    cur = 0
    stack = []

    def calculate(ch):
        nonlocal op, cur
        if op == "+":
            stack.append(cur)
        elif op == "-":
            stack.append(-cur)
        elif op == "*":
            stack[-1] *= cur
        elif op == "/":
            # 需要python 除法向 0 取整
            # python strange behavior: -3 // 2 = -2
            stack[-1] = int(stack[-1] / cur)
        cur = 0
        op = ch

    for i in range(n):
        if s[i].isdigit():
            cur = int(s[i]) + cur * 10
        else:
            calculate(s[i])
    calculate("") # last round
    return sum(stack)

correct = basicCalculatorII(s)
points = defaultdict(int)
points[correct] = 5
```

再來問題是該如何計算出那些計算順序錯誤而產生的值

將數值跟操作符依序分開會得到

stack = [X X X X X X X X X]
op    = [ Y Y Y Y Y Y Y Y ]

根據constraint: 1 <= len(op) <= 15

長度不長, 任意順序挑選operator並計算, 遞歸搜索出所有可能答案?
而我們在做的, 其實就是對任意operator加上括號優先計算, 而這其實就是[leetcode - 241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/description/)

以`s=2*3-4*5`為例:

```
(2)*(3-4*5)
    (2)*([3]-[4*5])
    (2)*([3-4]*[5])
(2*3)-(4*5)
(2*3-4)*(5)
    ([2*3]-4)*(5)
    (2*[3-4])*(5)
```

所以我們遍歷s[i]然後每當遇到operator就嘗試優先處理, 而我們遞歸返回的就是所有可能的計算答案
再根據運算符來將遞歸結果計算即可得到所有可能解
並將可能解放進hashset `res` 順便去重複

```py
n = len(s)
 
@cache
def dfs(l, r):
    if l == r: return {int(s[l:r+1])}
    
    res = set()

    for i in range(l, r+1):
        if s[i] in {"+", "*"}:
            left = dfs(l, i-1)
            right = dfs(i+1, r)

            if s[i] == "+":
                for x in left:
                    for y in right:
                        res.add(x+y)
            elif s[i] == "*":
                for x in left:
                    for y in right:
                        res.add(x*y)
    
    # edge case: 代表沒有任何operator
    if not res:
        res.add(int(s[l:r+1]))
    
    return res
```

所以最終答案計算一下後即可得到:

```py
possibles = dfs(0, n-1)
for possible in possibles:
    if possible == correct: continue
    points[possible] = 2

return sum(map(lambda x:points[x], answers))
```

但可惜的是以上算法會TLE, 並且很難察覺到底該如何改進
實際上這題最坑的就是必須細心看底下的constraint:

> Test data are generated such that the correct answer of the expression is in the range of [0, 1000].

所有學生給出來的答案不會超過1000, 所以我們在進行遞歸找出所有可能解時, 可以>1000的答案給排除掉

再來就是, 事實上這題只會有個位數digit, 因此在遞歸過程裡在遍歷s[i]找運算符時, 我們可以直接step=2去遍歷

```py
res = set()
for i in range(l+1, r+1, 2):
    left = dfs(l, i-1)
    right = dfs(i+1, r)

    if s[i] == "+":
        res |= {x+y for x in left for y in right if x+y <= 1000}
    elif s[i] == "*":
        res |= {x*y for x in left for y in right if x*y <= 1000}
if not res and (num:=int(s[l])) <= 1000:
    res.add(num)
```