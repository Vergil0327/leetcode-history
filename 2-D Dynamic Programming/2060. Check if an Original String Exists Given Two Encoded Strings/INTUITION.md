# Intuition

首先想到的是用dfs去explore所有可能, 類似像這樣dfs(i, j): True/False for s1[:i] == s2[:j] where i, j are index of s1, s2 respectively

但如果先別想i, j, 如果我們是這麼比較的話dfs(s1, s2)的話:

- digits其實就是產生`"*" * digits`, 其中"*"可以跟任意字母相匹配
- 所以如果一方是digits, 另一方:
    1. 也是digits => 相互數字消掉
    2. 是letters => digits相當於"*", 可以跟任意letter匹配掉
- 如果兩方都是letters, 就直接匹配看看行不行

最終肯定會遞歸到:
1. 兩方都匹配完, 返回True
2. 任一方匹配完成為empty string, 但另一方還留有letters, 那就匹配失敗返回False

可惜當初遞歸的規則想不清楚沒寫出來, 這邊[@HuifengGuan](https://www.youtube.com/watch?v=K6d524jDH3A&ab_channel=HuifengGuan)有清楚的影片詳解

我們alpha跟digit分開處理, 所以首先先對s1, s2預處理一下, 將alpha跟digit分開

ex. s1="x94", 預處理後變成["x", "94"]

```py
def parse(s):
    arr = []
    i = 0
    while i < len(s):
        if s[i].isalpha():
            arr.append(s[i])
        else:
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            arr.append(s[i:j])
            i = j-1
        i += 1
    return arr
s, t = parse(s1), parse(s2)
```

那再來我們就能進行我們的分類遞歸:

定義dfs(i, prefix_free_match1, j, prefix_free_match2): 返回True/False代表是否可以decode成功, 其中:
- i, j分別代表`s`, `t`當前處理的字符
- prefix_free_match代表當前有多少個任意配對的字符, 相當於有多少個"*"

那分類遞歸就這幾種形式:

1. 如果s[i].isdigit(), 我們分出所有可能的digit數目就知道s[i]可產生多少個任意配對的"*"
2. 同理, 如果s[j].isdigit()也是一樣

```py
def getNum(s):
    """
    "112"可分出: [112], [1,12], [11,2], [1,1,2]
    相當於有: 112個*, 1+12個*, 11+2個*, 1+1+2個*, 可以自由配對
    """
    num = int(s)

    if len(s) == 1:
        return [num]
    elif len(s) == 2:
        a, b = num//10, num%10
        return [a+b, num]
    else:
        a, b, c = num//100, (num//10)%10, num%10
        return [a+b+c, a*10+b+c, a+b*10+c, num]

if i < m and s[i].isdigit(): # 拆分出free_match1
    nums = getNum(s[i])
    for num in nums:
        if dfs(i+1, prefix_free_match1+num, j, prefix_free_match2): return True
    return False

if j < n and t[j].isdigit(): # 拆分出free_match1
    nums = getNum(t[j])
    for num in nums:
        if dfs(i, prefix_free_match1, j+1, prefix_free_match2+num): return True
    return False
```

3. 匹配`*跟*`, `"*跟alpha"`, `"alpha跟*"`, `"alpha 跟 alpha"`

```py
# 消掉開頭的"*"
if prefix_free_match1 > 0 and prefix_free_match2 > 0:
    common = min(prefix_free_match1, prefix_free_match2)
    return dfs(i, prefix_free_match1-common, j, prefix_free_match2-common)
elif prefix_free_match1 > 0:
    return dfs(i, prefix_free_match1-1, j+1, prefix_free_match2)
elif prefix_free_match2 > 0:
    return dfs(i+1, prefix_free_match1, j, prefix_free_match2-1)
else:
    if s[i] != t[j]: return False
    return dfs(i+1, 0, j+1, 0)
```

最後遞歸再配合memorization後即可

