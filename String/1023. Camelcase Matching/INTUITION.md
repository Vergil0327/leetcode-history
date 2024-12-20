# Intuition

我們的目標:我們能插入小寫字母到pattern, 然後檢查是否可以得到queries[i]
因此我們dfs去試著搜索看看能不能完成

首先base case很好想:

一但整個pattern用完, 檢查剩餘的queries[i]是否還留下任何大寫字母, 如果有那代表我們沒辦法透過插入小寫字母來使得pattern轉成queries[i]

```py
if j >= len(pattern):
    while s and s[0].islower():
        s = s[1:]
    return not s
```


再來就對pattern[j]來分大小寫討論:

1. 如果pattern[j]為大寫: 排除queries[i]的小寫後的第一個大寫必須符合
2. 如果pattern[j]為小寫: 遍歷queries[i]的小寫, 看有沒有符合. 如果queries[i]一路找, 找到所有小寫字母都不符合, 並且出現大寫字母, 那代表當前的pattern無法透過插入小寫字母轉成queries[i] (因為queries[i]不包含當前的queries[i]這個小寫字母)

```py
@cache
def check(s, j):
    if j >= len(pattern):
        while s and s[0].islower():
            s = s[1:]
        return not s

    if pattern[j].isupper():
        while s and s[0].islower():
            s = s[1:]
        if not s: return False

        if s[0] == pattern[j]:
            return check(s[1:], j+1)
        else:
            return False
    else:
        while s and s[0].islower():
            if s[0] == pattern[j]:
                j += 1
                return check(s[1:], j)
            
            s = s[1:]
        return False
```