# Intuition
對於每個integer來說, 必須是這樣的形式出現在sequence:
1: [1]
2: [2X2]
3: [3XX3]
4: [4XXX4]

sequence.size會是: 2*n-1
並且由於要lexicographically largest, 所以從n必須先放置在第一位
ex. [4 XXX 4]

然後我們在用dfs (backtracking)去搜索

**Greedy**

由於我們要**lexicographically largest**, 所以其實我們就逐位由大到小, 從n到1依序來試著放放看
不行再backtracking, 這樣一但我們找到第一個合法解, 就會是**lexicographically largest**的正解

```py
for num in range(n, 0, -1):
    if not valid: continue
    if dfs(i+1): return True
return False
```

not valid的情況有
- `num`已經使用過了
- 當`num > 1`時, arr[i+num]是不是存在並且還沒被使用過